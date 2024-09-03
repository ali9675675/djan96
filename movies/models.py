from django.db import models

# Create your models here.


class Movie(models.Model):
    # id -> starts at 1 and auto-increments
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=False)


# makemigrations -> create instructions telling django how the database have changed
# migrate -> applies the above changes
# CRUD operations -> create, read, update, delete
# model manager -> objects
# movie.objects.all()
# movie.objects.get(id=1)
# movie.objects.filter(title="movie title")
