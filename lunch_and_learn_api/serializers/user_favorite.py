from rest_framework import serializers
from lunch_and_learn_api.models import UserFavorite

class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = '__all__'