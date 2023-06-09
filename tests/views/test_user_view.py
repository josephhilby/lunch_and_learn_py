import json
import pytest
from django.test import RequestFactory, TestCase

from tests.factories import UserFactory
from lunch_and_learn_api.models import User
from lunch_and_learn_api.views import UserViewSet

class UserViewTests(TestCase):
  def test_user_get_one(self):
    user = UserFactory()
    request = RequestFactory().get(f"api/v1/user/{user.pk}")
    view = UserViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=user.pk)
    assert response.status_code == 200
    assert response.data['id'] == user.id


  def test_user_get_all(self):
    UserFactory.create_batch(3)
    request = RequestFactory().get(f"api/v1/user/")
    view = UserViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 3


  def test_user_post(self):
    user = { "name": "name", "email": "email", "password": "password", "api_key": "api_key" }
    request = RequestFactory().post("api/v1/user/", user)
    view = UserViewSet.as_view({'post': 'create'})
    assert not User.objects.exists()
    data = json.dumps(user)
    response = view(request, data)
    assert response.status_code == 201
    assert User.objects.count() == 1
    assert User.objects.get(pk = User.objects.last().pk).name == 'name'


  def test_user_delete(self):
    user = UserFactory()
    assert User.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/user/{user.pk}")
    view = UserViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=user.pk)
    assert not User.objects.exists()
    assert response.status_code == 204


  def test_user_patch(self):
    user = UserFactory(name='paul')
    user_update = { "data": { "type": "User", "id": f"{user.pk}", "attributes": {"name": "john" } } }
    data = json.dumps(user_update)
    request = RequestFactory().patch(f"api/v1/user/{user.pk}", data, content_type='application/vnd.api+json')
    view = UserViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=user.pk)
    updated_user = User.objects.get(pk = user.pk)
    assert updated_user.name == 'john'
    assert response.status_code == 200


  def test_user_404(self):
    user = UserFactory()
    request = RequestFactory().get(f"api/v1/user/{user.pk + 1}")
    view = UserViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=user.pk + 1)
    assert response.status_code == 404
