# Run project

```
docker-compose up
```

# Description

Django application to manage Book store. The core is store app. 

There are three endpoints : 

-"/api/shop_books/" to retrieve all books present in shop

-"/api/books_author/<int:pk>/" to retrieve all books of an author (in book table)

-"/api/new_edition/" to insert new edition of a book present in shop. When creating new edition, the price of the book in the shop automatically increases by 5%.

There are two initial import: 

-store/migrations/genre_initialization.py to initialize all possible Genre.

-sore/migrations/data_import.py to generate some data to use application.

When a new Instance of Shop is created, a reference to the latest edition of the book is automatically added.
