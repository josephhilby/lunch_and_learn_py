from django.db import models
from .user import User
from .favorite import Favorite

class UserFavorite(models.Model):
    class Meta:
        app_label = 'lunch_and_learn_api'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_id = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
