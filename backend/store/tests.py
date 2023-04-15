from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book, Edition, Genre, Shop
from datetime import date


class BookShopTestCase(APITestCase):
    def setUp(self):
        author = Author.objects.create(
            first_name="first_name_test",
            last_name="last_name_test",
            nationality=Author.TypeChoices.FR,
        )
        book = Book.objects.create(
            title="title_test", num_pages=235, genre=Genre.objects.first()
        )
        book.authors.add(author)
        Edition.objects.create(
            book=book, edition_number=1, publication_date=date.today()
        )
        Shop.objects.create(book=book, price=13.33)
        Book.objects.create(
            title="title_test_for_shop", num_pages=235, genre=Genre.objects.first()
        )

    def test_books_shop(self):
        response = self.client.get("/api/shop_books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_books_author(self):
        pk = Author.objects.first().pk
        response = self.client.get(f"/api/books_author/{pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_books_author_not_found(self):
        pk = Author.objects.last().pk + 1
        response = self.client.get(f"/api/books_author/{pk}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_new_edition(self):
        pk = Shop.objects.first().book.pk
        data = {"book": pk, "edition_number": 2, "publication_date": date.today()}
        response = self.client.post("/api/new_edition/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_new_edition_book_not_found(self):
        pk = Book.objects.last().pk + 1
        data = {"book": pk, "edition_number": 2, "publication_date": date.today()}
        response = self.client.post("/api/new_edition/", data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_new_edition_book_not_found_in_shop(self):
        pk = Shop.objects.order_by("-book__id").first().book.pk + 1
        data = {"book": pk, "edition_number": 2, "publication_date": date.today()}
        response = self.client.post("/api/new_edition/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_new_edition_bad_number(self):
        pk = Shop.objects.first().book.pk
        data = {"book": pk, "edition_number": 3, "publication_date": date.today()}
        response = self.client.post("/api/new_edition/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
