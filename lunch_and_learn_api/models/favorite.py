from django.db import models

class Favorite(models.Model):
    class Meta:
        app_label = 'lunch_and_learn_api'

    country = models.CharField(max_length=100)
    recipe_link = models.CharField(max_length=250)
    recipe_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
