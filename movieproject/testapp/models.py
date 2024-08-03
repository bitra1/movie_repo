from django.db import models

# Create your models here.
class MovieModel(models.Model):
    moviename = models.CharField(max_length=20)
    releasedate = models.DateField()
    heroname = models.CharField(max_length=20)
    heroinename = models.CharField(max_length=20)
    rating = models.IntegerField()

    
