from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    published_year = models.SmallIntegerField(default=2026)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title
