from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    class TypeChoices(models.TextChoices):
        IT = "IT", _("Italian")
        FR = "FR", _("French")
        GE = "GE", _("German")
        SP = "SP", _("Spanish")

    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    nationality = models.CharField(
        _("Nationality"), max_length=2, choices=TypeChoices.choices
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


"""
In migrations/genre_initialization.py is setted table population with default values. 
"""


class Genre(models.Model):
    class TypeChoices(models.TextChoices):
        FANTASY = "fantasy", _("Fantasy")
        NARRATIVE = "narrative", _("Narrative")
        THRILLER = "thriller", _("Thriller")
        CRIME = "crime", _("Crime")

    name = models.CharField(
        _("Name"),
        max_length=9,
        choices=TypeChoices.choices,
        unique=True,
        blank=False,
        null=False,
    )
    forbidden_to_minors = models.BooleanField(_("Forbidden to minors"), default=False)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    num_pages = models.PositiveIntegerField(_("Number of pages"))
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name="book_genre"
    )
    authors = models.ManyToManyField(Author, related_name="book_authors")

    def __str__(self) -> str:
        return self.title


class Edition(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book_edition"
    )
    edition_number = models.PositiveIntegerField(_("Edition number"), default=1)
    publication_date = models.DateField(_("Publication date"))

    def __str__(self) -> str:
        return f"Book : {self.book}. Edition number : {self.edition_number}"


"""
Before creating or updating an instance of Shop, is added a reference to last edition of book.
In signals.py is setted price update on new edition loading for book present in shop.
"""


class Shop(models.Model):
    book = models.OneToOneField(
        Book, on_delete=models.PROTECT, related_name="shop_book"
    )
    edition = models.OneToOneField(
        Edition, on_delete=models.PROTECT, related_name="shop_edition", editable=False
    )
    price = models.FloatField(_("Price"))

    def save(self, *args, **kwargs):
        try:
            e = self.book.book_edition.order_by("-edition_number").first()
            self.edition = e
        except:
            raise Exception("This book has no editions!")
        self.price = round(self.price, 2)
        super(Shop, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Book : {self.edition.book}. Price : {self.price}"
