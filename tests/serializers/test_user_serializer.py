import pytest
from datetime import datetime
from django.test import TestCase

from tests.factories import UserFactory
from lunch_and_learn_api.serializers import UserSerializer

class UserSerializerTests(TestCase):
    def test_user_serializer(self):
        user = UserFactory()
        serialized_user = UserSerializer(user).data

        assert isinstance(serialized_user, dict)
        assert len(serialized_user) == 7

        assert serialized_user['id'] == user.id
        assert isinstance(serialized_user['id'], int)

        assert serialized_user['name'] == user.name
        assert isinstance(serialized_user['name'], str)

        assert serialized_user['email'] == user.email
        assert isinstance(serialized_user['email'], str)

        assert serialized_user['password'] == user.password
        assert isinstance(serialized_user['password'], str)

        assert serialized_user['api_key'] == user.api_key
        assert isinstance(serialized_user['api_key'], str)

        assert serialized_user['created_at'] == user.created_at.isoformat()
        assert isinstance(serialized_user['created_at'], str)

        assert serialized_user['updated_at'] == user.updated_at.isoformat()
        assert isinstance(serialized_user['updated_at'], str)
