from django.shortcuts import render
from rest_framework import viewsets
from lunch_and_learn_api.models import Favorite
from lunch_and_learn_api.serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
