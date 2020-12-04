from django.db import models


class Product(models.Model):
  name = models.CharField(max_length=150)
  price = models.IntegerField()
  description = models.TextField()
  thumbnail = models.ImageField(upload_to="thumbnails/")