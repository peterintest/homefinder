from django.contrib.auth.hashers import make_password
from accounts.tests.factories import UserFactory
from listings.tests.factories import ListingFactory
import pytest

TEST_USERNAME = 'username1'
TEST_PASSWORD = 'password1'

@pytest.fixture()
def user(db):
    """Add a test user to the database."""
    _user = UserFactory.create(
        username = TEST_USERNAME,
        password = TEST_PASSWORD
    )
    return _user


@pytest.fixture
def authenticated_user(user, client):
    """Authenticate user"""
    client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
    return user


@pytest.fixture()
def listing(db):
    """Add a test listing to the database."""
    return ListingFactory.create()
