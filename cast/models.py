from django.db import models


class Cast(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=255)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='cast_images')
    date_of_birth = models.DateField()
    full_bio = models.TextField(max_length=2000)
    birth_place = models.CharField(max_length=120)
    birth_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    quote = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
    

class CastImage(models.Model):
    image = models.ImageField(upload_to='cast_extra_images')
    cast_id = models.ForeignKey(Cast, on_delete=models.CASCADE, related_name='images')