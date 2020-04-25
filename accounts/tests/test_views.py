from django import urls
from contacts.models import Contact
from django.contrib.auth.models import User
import pytest

pytestmark = pytest.mark.unittest

def test_login_and_logout(client, user):
    # login
    login_url = urls.reverse('login')
    resp = client.post(login_url, {
        'username': user.username,
        'password': 'password1'
    })
    assert resp.status_code == 302
    assert resp.url == urls.reverse('index')

    # logout
    logout_url = urls.reverse('logout')
    resp = client.post(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('index')


def test_invalid_login(client, db):
    # login
    login_url = urls.reverse('login')
    resp = client.post(login_url, {
        'username': 'username1',
        'password': 'password1'
    })
    assert resp.status_code == 200
    assert b'Login' in resp.content


def test_access_login_page(client, db):
    url = urls.reverse('login')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Login' in resp.content 


def test_access_register_page(client, db):
    url = urls.reverse('register')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Register' in resp.content 


def test_register(client, db):
    url = urls.reverse('register')
    resp = client.post(url, {
        'firstname': 'David',
        'lastname': 'Jones',
        'username': 'username1',
        'email': 'email@test.com',
        'password': 'password1',
        'password2': 'password1'
    })
    assert resp.status_code == 302
    assert resp.url == urls.reverse('login')


def test_register_mismatching_passwords(client, db):
    url = urls.reverse('register')
    resp = client.post(url, {
        'firstname': 'David',
        'lastname': 'Jones',
        'username': 'username1',
        'email': 'email@test.com',
        'password': 'password1',
        'password2': 'password2'
    })
    assert resp.status_code == 200
    assert b'Register' in resp.content


def test_register_existing_email(client, user):
    url = urls.reverse('register')
    resp = client.post(url, {
        'firstname': 'David',
        'lastname': 'Jones',
        'username': 'username2',
        'email': 'email@test.com',
        'password': 'password1',
        'password2': 'password1'
    })
    assert resp.status_code == 200
    assert b'Register' in resp.content


def test_register_existing_username(client, user):
    url = urls.reverse('register')
    resp = client.post(url, {
        'firstname': 'David',
        'lastname': 'Jones',
        'username': 'username1',
        'email': 'test@test.com',
        'password': 'password1',
        'password2': 'password1'
    })
    assert resp.status_code == 200
    assert b'Register' in resp.content


def test_access_dashboard_page(client, db, authenticated_user):
    url = urls.reverse('dashboard')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Dashboard' in resp.content 

def test_access_dashboard_page_unauthenticated(client, db):
    url = urls.reverse('dashboard')
    resp = client.get(url)
    assert resp.status_code == 403
    assert b'Forbidden' in resp.content 
