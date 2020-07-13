from django.db import models
from multiselectfield import MultiSelectField


class Movie(models.Model):
    name = models.CharField(max_length = 50)
    imdb_score = models.FloatField()
    director = models.CharField(max_length = 50)
    popularity = models.FloatField()
    genre_choices = (
        ('Adventure', 'Adventure'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Musical', 'Musical'),
        ('Suspense', 'Suspense'),
        ('Drama', 'Drama'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Action', 'Action'),
        ('Mystrey', 'Mystrey')
    )
    genre = MultiSelectField(max_length=100, choices=genre_choices)
    def __str__(self):
        return self.name

class Users(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True )
    password = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.first_name