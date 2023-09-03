from django.contrib import admin

from . import models

admin.site.register(models.Movie)
admin.site.register(models.MovieTag)
admin.site.register(models.MovieGenre)
admin.site.register(models.Review)