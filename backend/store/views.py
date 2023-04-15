from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .serializers import ShopSerializer, BookSerializer, EditionCreateSerializer
from .models import Shop, Book, Author, Edition
from django.shortcuts import get_object_or_404
from .pagination import CustomPaginationAuthor
from .exceptions import NotBook, NotBookInShop

"""
View to retrieve list of all books in Shop. 
"""


class ShopListAPIView(generics.ListAPIView):
    queryset = Shop.objects.order_by("book__title", "book__genre__name")
    serializer_class = ShopSerializer


"""
View to retrieve list of books of an Author given his pk passed as path parameter. 
"""


class BookAuthorDetailListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    pagination_class = CustomPaginationAuthor

    def get_object(self):
        author = get_object_or_404(Author, pk=self.kwargs.get("pk"))
        return author

    def get_queryset(self):
        author = self.get_object()
        books = Book.objects.filter(authors__in=[author]).order_by("title")
        return books

    def list(self, request, pk):
        author = self.get_object()
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = {}
            result["author"] = f"{author.first_name} {author.last_name}"
            result["books"] = serializer.data
            return self.get_paginated_response(result)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


""" 
View for new edition for book present in shop. 
Body of request must be : 
{
"book" : int, #book_id
"edition_number": int, 
"publication_date": "YYYY-MM-DD"
}
"""


class NewEditionShopBookAPIView(APIView):
    def post(self, request):
        try:
            book = Book.objects.get(id=request.data.get("book"))
        except:
            raise NotBook()
        if len(Shop.objects.filter(book=book)) == 0:
            raise NotBookInShop()
        edition_qs = (
            Edition.objects.filter(book=book).order_by("-edition_number").first()
        )
        if edition_qs.edition_number + 1 != int(request.data.get("edition_number")):
            raise ValidationError(
                detail=f"edition_number must be one greater than the current one. Current edition_number is : {edition_qs.edition_number}"
            )
        serializer = EditionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
