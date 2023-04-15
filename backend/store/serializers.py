from rest_framework import serializers
from .models import Shop, Book, Edition, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "nationality"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name", "forbidden_to_minors"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = ["title", "num_pages", "genre", "authors"]


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ["edition_number", "publication_date"]


class ShopSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    edition = EditionSerializer()

    class Meta:
        model = Shop
        fields = ["book", "edition", "price"]


class EditionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ["book", "edition_number", "publication_date"]
