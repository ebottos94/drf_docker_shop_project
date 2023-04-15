from rest_framework.exceptions import APIException
from rest_framework import status


class NotBook(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "No book found with this book id"
    default_code = "no_book"


class NotBookInShop(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This book is not present in shop"
    default_code = "no_book_in_shop"
