from django.shortcuts import render
from rest_framework import viewsets
from lunch_and_learn_api.models import User
from lunch_and_learn_api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
