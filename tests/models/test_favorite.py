import pytest
from django.test import TestCase
from tests.factories import FavoriteFactory
from lunch_and_learn_api.models import Favorite

class FavoriteTests(TestCase):
    def setUp(self):
        self.favorite = FavoriteFactory(
            country='country',
            recipe_link='recipe_link',
            recipe_title='recipe_title'
        )


    def test_favorite_instance(self):
        assert isinstance(self.favorite, Favorite)


    def test_favorite_state(self):
        assert self.favorite.country == 'country'
        assert self.favorite.recipe_link == 'recipe_link'
        assert self.favorite.recipe_title == 'recipe_title'