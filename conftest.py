from django.contrib.auth.models import User
import pytest

@pytest.fixture
def authenticated_user(client):
    """Create an authenticated user for a test"""
    # create user
    user = User.objects.create_user(username='username1',
                                    password='password1',
                                    email='test@test.com',
                                    first_name='David',
                                    last_name='Jones')
    user.save()
    client.login(username='username1', password='password1')
    return user
