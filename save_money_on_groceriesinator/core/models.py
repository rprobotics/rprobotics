from django.db import models

# Create your models here.

class Ingredient(models.Model):
    # the same ingredient will be used by many people, and recipes
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    # Recipes use multiple ingredients
    ingredList = models.ManyToManyField(Ingredient,
                                        through='RecipeIngredient',
                                        through_fields=('recipe', 'ingredient'))
    directions = models.TextField()
    title      = models.CharField(max_length=100)
    #original_url = models.URLField()


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=25)


class Pantry(models.Model):
    owner = models.CharField(max_length=50)
    ingredList = models.ManyToManyField(Ingredient,
                                        through='PantryIngredient',
                                        through_fields=('pantry', 'ingredient'))

class PantryIngredient(models.Model):
    name = models.CharField(max_length=50)
    pantry = models.ForeignKey(Pantry)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=25)
