from django.db import models

# Create your models here.
class Yoga(models.Model):
    yoganame = models.CharField(max_length=100)
    img =  models.ImageField(upload_to='yoga_pics')
    yogasteps = models.TextField()
    yogadetails = models.TextField()
    noOfmins = models.IntegerField()