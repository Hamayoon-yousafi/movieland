from django.db import models


class Cast(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=255)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='cast_images')
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name