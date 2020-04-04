from django import urls
import pytest


def test_home_page(client, db):
    url = urls.reverse('index')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Find Your New Home' in resp.content


def test_about_page(client):
    url = urls.reverse('about')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'About Home Finder' in resp.content
