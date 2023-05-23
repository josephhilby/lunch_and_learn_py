import factory
from faker import Factory as FakerFactory

from lunch_and_learn_api.models import User, Favorite, UserFavorite

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())
    api_key = factory.LazyAttribute(lambda x: faker.password())

    class Meta:
        model = User


class FavoriteFactory(factory.django.DjangoModelFactory):
    country = factory.LazyAttribute(lambda x: faker.country())
    recipe_link = factory.LazyAttribute(lambda x: faker.url())
    recipe_title = factory.LazyAttribute(lambda x: faker.sentence())

    class Meta:
        model = Favorite


class UserFavoriteFactory(factory.django.DjangoModelFactory):
    user_id = factory.SubFactory(UserFactory)
    favorite_id = factory.SubFactory(FavoriteFactory)

    class Meta:
        model = UserFavorite