from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    profile_picture = models.ImageField(blank=True, null=True, upload_to='user_profiles')
    favorite_genre = models.ForeignKey('movies.MovieGenre', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return '/static/img/blank_profile.jpg'
    # def __str__(self):
    #     return self.user