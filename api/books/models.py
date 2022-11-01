from django.db import models

# Create your models here.


class BookData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default='favorites')
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')