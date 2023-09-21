from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

VOTE_TYPE = (
    ('up', 'Up Vote'),
    ('down', 'Down Vote')
)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    story = models.TextField(max_length=500)
    release_date = models.DateField()
    movie_file = models.FileField(upload_to='movies/%y-%m-%d', blank=True, null=True)
    thumbnail = models.FileField(upload_to='thumbnails/%y-%m-%d')
    poster = models.FileField(upload_to='posters/%y-%m-%d')
    trailer = models.FileField(upload_to='trailers/%y-%m-%d', blank=True, null=True)
    subtitle = models.FileField(upload_to='subtitles/%y-%m-%d', blank=True, null=True)
    genre_ids = models.ManyToManyField('MovieGenre', verbose_name='Genres')
    tag_ids = models.ManyToManyField('MovieTag', verbose_name='Tags')
    cast_ids = models.ManyToManyField('cast.Cast', verbose_name='Casts', related_name='movies')
    total_positive_votes = models.IntegerField(editable=False, default=0)
    total_negative_votes = models.IntegerField(editable=False, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True, max_length=255)
    vote = models.CharField(max_length=255, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.vote == 'up':
            self.movie_id.total_positive_votes += 1
        else:
            self.movie_id.total_negative_votes += 1
        self.movie_id.save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.vote
    
    class Meta:
        unique_together = [['user_id', 'movie_id']]


class MovieGenre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    @property
    def get_update_url(self):
        return reverse('genre-update', args=[self.id])
    
    @property
    def get_delete_url(self):
        return reverse('genre-delete', args=[self.id])


class MovieTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    @property
    def get_update_url(self):
        return reverse('tag-update', args=[self.id])
    
    @property
    def get_delete_url(self):
        return reverse('tag-delete', args=[self.id])