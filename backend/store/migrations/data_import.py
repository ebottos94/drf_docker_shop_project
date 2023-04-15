from django.db import migrations
from datetime import date


def import_data(apps, schema_editor):
    Author = apps.get_model("store", "Author")
    Book = apps.get_model("store", "Book")
    Genre = apps.get_model("store", "Genre")
    Edition = apps.get_model("store", "Edition")
    Shop = apps.get_model("store", "Shop")

    a1 = Author.objects.create(
        first_name="Giuseppe", last_name="Ferrandino", nationality="IT"
    )
    a2 = Author.objects.create(
        first_name="Michel", last_name="Houellebecq", nationality="FR"
    )
    a3 = Author.objects.create(first_name="Herta", last_name="Müller", nationality="GE")
    a4 = Author.objects.create(
        first_name="Fernando", last_name="Aramburu", nationality="SP"
    )
    narrative = Genre.objects.get(name="narrative")
    crime = Genre.objects.get(name="crime")
    b1 = Book.objects.create(title="Pericle il Nero", num_pages=144, genre=crime)
    b1.authors.add(a1)
    b2 = Book.objects.create(title="Il Rispetto", num_pages=120, genre=crime)
    b2.authors.add(a1)
    b3 = Book.objects.create(title="Sérotonine", num_pages=332, genre=narrative)
    b3.authors.add(a2)
    b4 = Book.objects.create(title="Soumission", num_pages=252, genre=narrative)
    b4.authors.add(a2)
    b5 = Book.objects.create(title="Atemschaukel", num_pages=304, genre=narrative)
    b5.authors.add(a3)
    b6 = Book.objects.create(
        title="Die blassen Herren mit den Mokkatassen", num_pages=112, genre=narrative
    )
    b6.authors.add(a3)
    b7 = Book.objects.create(title="Patria", num_pages=640, genre=narrative)
    b7.authors.add(a4)
    b8 = Book.objects.create(title="Los vencejos", num_pages=720, genre=narrative)
    b8.authors.add(a4)
    publication_date = date(1998, 5, 20)
    e1 = Edition.objects.create(
        book=b1, edition_number=1, publication_date=publication_date
    )
    publication_date = date(1999, 5, 12)
    e2 = Edition.objects.create(
        book=b2, edition_number=1, publication_date=publication_date
    )
    publication_date = date(2019, 1, 10)
    e3 = Edition.objects.create(
        book=b3, edition_number=1, publication_date=publication_date
    )
    publication_date = date(2018, 6, 20)
    e4 = Edition.objects.create(
        book=b4, edition_number=1, publication_date=publication_date
    )
    publication_date = date(2011, 6, 8)
    e5 = Edition.objects.create(
        book=b5, edition_number=1, publication_date=publication_date
    )
    publication_date = date(2005, 8, 8)
    e6 = Edition.objects.create(
        book=b6, edition_number=1, publication_date=publication_date
    )
    publication_date = date(2019, 8, 27)
    e7 = Edition.objects.create(
        book=b7, edition_number=1, publication_date=publication_date
    )
    publication_date = date(2021, 8, 25)
    e8 = Edition.objects.create(
        book=b8, edition_number=1, publication_date=publication_date
    )
    Shop.objects.create(book=b1, edition=e1, price=11.40)
    Shop.objects.create(book=b2, edition=e2, price=12.00)
    Shop.objects.create(book=b3, edition=e3, price=19.00)
    Shop.objects.create(book=b4, edition=e4, price=17.50)
    Shop.objects.create(book=b5, edition=e5, price=13.00)
    Shop.objects.create(book=b6, edition=e6, price=19.00)
    Shop.objects.create(book=b7, edition=e7, price=13.95)
    Shop.objects.create(book=b8, edition=e8, price=25.01)


class Migration(migrations.Migration):
    dependencies = [
        ("store", "genre_initialization"),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
