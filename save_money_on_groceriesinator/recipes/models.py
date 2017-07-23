from django.db import models

# Create your models here.
class Recipes(models.Model):
    class Meta:
        app_label = 'recipe'
    ingredList = models.TextField()
    directions = models.TextField()
    title      = models.TextField()


