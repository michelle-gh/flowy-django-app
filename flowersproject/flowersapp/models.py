from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


class Flower(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = cloudinary.models.CloudinaryField(
        folder='media/flower_images/', overwrite=True, resource_type='', blank=True)

    def __str__(self):
        return self.name


