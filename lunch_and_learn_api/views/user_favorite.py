from django.shortcuts import render
from rest_framework import viewsets
from lunch_and_learn_api.models import UserFavorite
from lunch_and_learn_api.serializers import UserFavoriteSerializer

class UserFavoriteViewSet(viewsets.ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer
