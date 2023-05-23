import pytest
from django.test import TestCase
from tests.factories import UserFactory
from lunch_and_learn_api.models import User

class UserTests(TestCase):
    def setUp(self):
        self.user = UserFactory(
            name='name',
            email='email',
            password='password',
            api_key='api_key'
        )


    def test_user_instance(self):
        assert isinstance(self.user, User)


    def test_user_state(self):
        assert self.user.name == 'name'
        assert self.user.email == 'email'
        assert self.user.password == 'password'
        assert self.user.api_key == 'api_key'