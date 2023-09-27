from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    favorite_genre = models.ForeignKey('movies.MovieGenre', on_delete=models.SET_NULL, null=True, blank=True)

    # def __str__(self):
    #     return self.user