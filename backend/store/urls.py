from django.urls import path
from .views import (
    ShopListAPIView,
    BookAuthorDetailListAPIView,
    NewEditionShopBookAPIView,
)

urlpatterns = [
    path("shop_books/", ShopListAPIView.as_view(), name="shoop_books_api"),
    path(
        "books_author/<int:pk>/",
        BookAuthorDetailListAPIView.as_view(),
        name="books_author",
    ),
    path(
        "new_edition/",
        NewEditionShopBookAPIView.as_view(),
        name="new_shop_book_edition",
    ),
]
