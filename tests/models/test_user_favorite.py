import pytest
from django.test import TestCase
from tests.factories import UserFactory, FavoriteFactory, UserFavoriteFactory
from lunch_and_learn_api.models import User, Favorite, UserFavorite

class UserFavoriteTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.favorite = FavoriteFactory()

        self.user_favorite = UserFavoriteFactory(
            user_id=self.user,
            favorite_id=self.favorite
        )


    def test_user_favorite_instance(self):
        assert isinstance(self.user_favorite, UserFavorite)


    def test_user_favorite_state(self):
        assert self.user_favorite.user_id == self.user
        assert self.user_favorite.favorite_id == self.favorite