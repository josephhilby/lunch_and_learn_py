from django.contrib import admin
from .models import User, Favorite, UserFavorite

admin.site.register(User)
admin.site.register(Favorite)
admin.site.register(UserFavorite)
