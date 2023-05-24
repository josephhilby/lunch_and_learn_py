import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import FavoriteFactory
from lunch_and_learn_api.models import Favorite
from lunch_and_learn_api.views import FavoriteViewSet

class FavoriteViewTests(TestCase):
  def test_favorite_get_one(self):
    favorite = FavoriteFactory()
    request = RequestFactory().get(f"api/v1/favorite/{favorite.pk}")
    view = FavoriteViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=favorite.pk)
    assert response.status_code == 200
    assert response.data['id'] == favorite.id


  def test_favorite_get_all(self):
    FavoriteFactory.create_batch(3)
    request = RequestFactory().get(f"api/v1/favorite/")
    view = FavoriteViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 3


  def test_favorite_post(self):
    favorite = { "country": "country", "recipe_link": "recipe_link", "recipe_title": "recipe_title" }
    request = RequestFactory().post("api/v1/favorite/", favorite)
    view = FavoriteViewSet.as_view({'post': 'create'})
    assert not Favorite.objects.exists()
    data = json.dumps(favorite)
    response = view(request, data)
    assert response.status_code == 201
    assert Favorite.objects.count() == 1
    assert Favorite.objects.get(pk = Favorite.objects.last().pk).country == 'country'


  def test_favorite_delete(self):
    favorite = FavoriteFactory()
    assert Favorite.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/favorite/{favorite.pk}")
    view = FavoriteViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=favorite.pk)
    assert not Favorite.objects.exists()
    assert response.status_code == 204


  def test_favorite_patch(self):
    favorite = FavoriteFactory(country='india')
    favorite_update = { "data": { "type": "Favorite", "id": f"{favorite.pk}", "attributes": {"country": "japan" } } }
    data = json.dumps(favorite_update)
    request = RequestFactory().patch(f"api/v1/favorite/{favorite.pk}", data, content_type='application/vnd.api+json')
    view = FavoriteViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=favorite.pk)
    updated_favorite = Favorite.objects.get(pk = favorite.pk)
    assert updated_favorite.country == 'japan'
    assert response.status_code == 200


  def test_favorite_404(self):
    favorite = FavoriteFactory()
    request = RequestFactory().get(f"api/v1/favorite/{favorite.pk + 1}")
    view = FavoriteViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=favorite.pk + 1)
    assert response.status_code == 404
