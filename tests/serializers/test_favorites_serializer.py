import pytest
from datetime import datetime
from django.test import TestCase

from tests.factories import FavoriteFactory
from lunch_and_learn_api.serializers import FavoriteSerializer

class FavoriteSerializerTests(TestCase):
    def test_favorite_serializer(self):
        favorite = FavoriteFactory()
        serialized_favorite = FavoriteSerializer(favorite).data

        assert isinstance(serialized_favorite, dict)
        assert len(serialized_favorite) == 6

        assert serialized_favorite['id'] == favorite.id
        assert isinstance(serialized_favorite['id'], int)

        assert serialized_favorite['country'] == favorite.country
        assert isinstance(serialized_favorite['country'], str)

        assert serialized_favorite['recipe_link'] == favorite.recipe_link
        assert isinstance(serialized_favorite['recipe_link'], str)

        assert serialized_favorite['recipe_title'] == favorite.recipe_title
        assert isinstance(serialized_favorite['recipe_title'], str)

        assert serialized_favorite['created_at'] == favorite.created_at.isoformat()
        assert isinstance(serialized_favorite['created_at'], str)

        assert serialized_favorite['updated_at'] == favorite.updated_at.isoformat()
        assert isinstance(serialized_favorite['updated_at'], str)
