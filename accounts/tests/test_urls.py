from django import urls
import pytest

pytestmark = pytest.mark.unittest

def test_register_url():
    url = urls.reverse('register')
    assert urls.resolve(url).view_name == 'register'


def test_login_url():
    url = urls.reverse('login')
    assert urls.resolve(url).view_name == 'login'


def test_logout_url():
    url = urls.reverse('logout')
    assert urls.resolve(url).view_name == 'logout'


def test_dashboard_url():
    url = urls.reverse('dashboard')
    assert urls.resolve(url).view_name == 'dashboard'
