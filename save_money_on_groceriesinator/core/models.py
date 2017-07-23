from django.db import models

# Create your models here.
class Recipes(models.Model):
    # Recipes use multiple ingredients
    ingredList = models.TextField()
    #ingredList =
    directions = models.TextField()
    title      = models.TextField()
    #original_url = models.URLField()


class Pantry(models.Model):
    # pantries have multiple ingredients
    pass


class Ingredient(models.Model):
    # the same ingredient will be used by many people, and recipes
    pantry = models.ManyToManyField(Pantry)
    recipe = models.ManyToManyField(Recipes)
    amount = models.PositiveSmallIntegerField()

class Recipe_Ingredient(models.Model):
    pass