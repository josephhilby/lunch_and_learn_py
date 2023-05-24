from rest_framework import serializers
from lunch_and_learn_api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
