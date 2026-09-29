from django.urls import path

from .views import GenreAPIView, BookAPIView

urlpatterns = [
    path('genres/', GenreAPIView.as_view()),
    path('books/', BookAPIView.as_view()),
]
