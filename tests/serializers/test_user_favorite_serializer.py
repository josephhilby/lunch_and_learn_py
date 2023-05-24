import pytest
from django.test import TestCase

from lunch_and_learn_api.models import UserFavorite
from lunch_and_learn_api.serializers import UserFavoriteSerializer
from tests.factories import UserFactory, FavoriteFactory, UserFavoriteFactory

class UserFavoriteSerializerTests(TestCase):
    def test_user_favorite_serializer(self):
        user = UserFactory()
        favorite = FavoriteFactory()
        user_favorite = UserFavoriteFactory(
            user_id=user,
            favorite_id=favorite
        )

        serialized_user_favorite = UserFavoriteSerializer(user_favorite).data

        assert isinstance(serialized_user_favorite, dict)
        assert len(serialized_user_favorite) == 5

        assert serialized_user_favorite['id'] == user_favorite.id
        assert isinstance(serialized_user_favorite['id'], int)

        assert serialized_user_favorite['user_id'] == user_favorite.user_id.id
        assert isinstance(serialized_user_favorite['user_id'], int)

        assert serialized_user_favorite['favorite_id'] == user_favorite.favorite_id.id
        assert isinstance(serialized_user_favorite['favorite_id'], int)

        assert serialized_user_favorite['created_at'] == user_favorite.created_at.isoformat()
        assert isinstance(serialized_user_favorite['created_at'], str)

        assert serialized_user_favorite['updated_at'] == user_favorite.updated_at.isoformat()
        assert isinstance(serialized_user_favorite['updated_at'], str)