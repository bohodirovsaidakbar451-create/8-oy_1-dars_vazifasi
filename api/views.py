from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Genre, Book
from django.forms import model_to_dict
from django.core.exceptions import ValidationError

class GenreAPIView(APIView):
    def get(self, request: Request):
        genres = Genre.objects.all()
        genres_list = []

        for genre in genres:
            genres_list.append(
                {
                    "id": genre.id,
                    "name": genre.name
                }
            )

        return Response(genres_list)

    def post(self, request: Request):
        name = request.data.get("name")

        if not name:
            return Response({"error": "name maydoni majburiy"}, status=400)

        if Genre.objects.filter(name=name).exists():
            return Response({"error": "Bunday janr allaqachon mavjud"}, status=400)

        genre = Genre.objects.create(name=name)
        genre_dict = model_to_dict(genre)
        return Response(genre_dict, status=201)


class BookAPIView(APIView):
    def get(self, request: Request):
        books = Book.objects.all()
        books_list = []

        for book in books:
            books_list.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "price": book.price,
                    "published_year": book.published_year,
                    "description": book.description,
                    "genre_id": book.genre.id if book.genre else None
                }
            )

        return Response(books_list)

    def post(self, request: Request):
        title = request.data.get("title")
        author = request.data.get("author")
        genre_id = request.data.get("genre_id")

        if not title or not author:
            return Response({"error": "title va author maydonlari majburiy"}, status=400)

        genre = None
        if genre_id:
            genre = Genre.objects.filter(id=genre_id).first()
            if genre is None:
                return Response({"error": "Bunday janr topilmadi"}, status=404)

        try:
            book = Book.objects.create(
                title=title,
                author=author,
                price=request.data.get("price", 0),
                published_year=request.data.get("published_year", 2026),
                description=request.data.get("description"),
                genre=genre
            )
        except (ValueError, ValidationError):
            return Response({"error": "price va published_year raqam bo'lishi kerak"}, status=400)

        book.refresh_from_db()
        book_dict = model_to_dict(book)
        return Response(book_dict, status=201)
