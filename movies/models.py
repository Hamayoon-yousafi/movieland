from django.db import models
import datetime


class Movie(models.Model):
    title = models.CharField(max_length=200)
    story = models.TextField(max_length=500)
    release_date = models.DateField()
    movie_file = models.FileField(upload_to='movies/%y-%m-%d')
    thumbnail = models.FileField(upload_to='thumbnails/%y-%m-%d')
    trailer = models.FileField(upload_to='trailers/%y-%m-%d')
    subtitle = models.FileField(upload_to='subtitles/%y-%m-%d')
    genre_ids = models.ManyToManyField('MovieGenre', verbose_name='Genres')
    tag_ids = models.ManyToManyField('MovieTag', verbose_name='Tags')

    def __str__(self):
        return self.title

class MovieGenre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MovieTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name