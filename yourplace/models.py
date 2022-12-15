from django.db import models

# Create your models here.
class Yoga(models.Model):
    yoganame = models.CharField(max_length=100)
    yogaimg =  models.ImageField(upload_to='yoga_pics')
    yogasteps = models.TextField()
    yogadetails = models.TextField()
    yoganoOfmins = models.IntegerField()

class Exercises(models.Model):
    exercisename = models.CharField(max_length=100)
    exerciseimg =  models.ImageField(upload_to='exercise_pics')
    exercisesteps = models.TextField()
    exercisedetails = models.TextField()
    exercisenoOfmins = models.IntegerField()    

class Recipes(models.Model):
    recipename = models.CharField(max_length=100)
    recipeimg =  models.ImageField(upload_to='recipes_pics')
    recipesteps = models.TextField()
    recipedetails = models.TextField()
    recipesnoOfmins = models.IntegerField()    