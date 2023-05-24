import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import UserFactory, FavoriteFactory, UserFavoriteFactory
from lunch_and_learn_api.models import UserFavorite
from lunch_and_learn_api.views import UserFavoriteViewSet

class UserFavoriteViewTests(TestCase):
  def test_user_favorite_get_one(self):
    user_favorite = UserFavoriteFactory()
    request = RequestFactory().get(f"api/v1/user_favorite/{user_favorite.pk}")
    view = UserFavoriteViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=user_favorite.pk)
    assert response.status_code == 200
    assert response.data['id'] == user_favorite.id


  def test_user_favorite_get_all(self):
    UserFavoriteFactory.create_batch(3)
    request = RequestFactory().get(f"api/v1/user_favorite/")
    view = UserFavoriteViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 3


  def test_user_favorite_post(self):
    user = UserFactory()
    favorite = FavoriteFactory()
    user_favorite = { "user_id": f"{user.pk}", "favorite_id": f"{favorite.pk}" }
    request = RequestFactory().post("api/v1/user_favorite/", user_favorite)
    view = UserFavoriteViewSet.as_view({'post': 'create'})
    assert not UserFavorite.objects.exists()
    data = json.dumps(user_favorite)
    response = view(request, data)
    assert response.status_code == 201
    assert UserFavorite.objects.count() == 1
    assert UserFavorite.objects.get(pk = UserFavorite.objects.last().pk).user_id.id == user.pk


  def test_user_favorite_delete(self):
    user_favorite = UserFavoriteFactory()
    assert UserFavorite.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/user_favorite/{user_favorite.pk}")
    view = UserFavoriteViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=user_favorite.pk)
    assert not UserFavorite.objects.exists()
    assert response.status_code == 204


  def test_user_favorite_patch(self):
    user_1 = UserFactory()
    user_2 = UserFactory()
    user_favorite = UserFavoriteFactory(user_id=user_1)
    user_favorite_update = { "data": { "type": "UserFavorite", "id": f"{user_favorite.pk}", "attributes": { "user_id": f"{user_2.pk}" } } }
    data = json.dumps(user_favorite_update)
    request = RequestFactory().patch(f"api/v1/user_favorite/{user_favorite.pk}", data, content_type='application/vnd.api+json')
    view = UserFavoriteViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=user_favorite.pk)
    updated_favorite = UserFavorite.objects.get(pk = user_favorite.pk)
    updated_favorite.user_id.id == user_2.pk
    assert response.status_code == 200


  def test_favorite_404(self):
    user_favorite = UserFavoriteFactory()
    request = RequestFactory().get(f"api/v1/user_favorite/{user_favorite.pk + 1}")
    view = UserFavoriteViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=user_favorite.pk + 1)
    assert response.status_code == 404
