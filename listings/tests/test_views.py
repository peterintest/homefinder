from django import urls
from django.contrib.auth.models import AnonymousUser
from listings.views import index, listing, search, Search
from .factories import ListingFactory
import pytest

pytestmark = pytest.mark.unittest

def test_listings(client, listing):
    url = urls.reverse('listings')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Our Properties' in resp.content


def test_listing_details(client, listing):
    url = urls.reverse('listing', kwargs={'listing_id': listing.id})
    resp = client.get(url)
    assert resp.status_code == 200


def test_listing_with_missing_thumbnail(client, db):
    listing = ListingFactory.create(photo_1=None)
    url = urls.reverse('listing', kwargs={'listing_id': listing.id})
    resp = client.get(url)
    assert resp.status_code == 200


def test_search_no_listings(client, db):
    url = urls.reverse('search')
    resp = client.get(url)
    assert b'No listings found' in resp.content
    assert resp.status_code == 200


def test_search_by_keyword(client, listing):
    listing = ListingFactory.create(city='Oxford')
    url = urls.reverse('search')
    resp = client.get(url, {
        'keywords': listing.city
    })
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_filter_by_num_bedrooms(client, db):
    listing = ListingFactory.create(bedrooms=3)
    url = urls.reverse('search')
    resp = client.get(url, {
        'bedrooms': listing.bedrooms
    })
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_filter_by_max_price(client, db):
    listing = ListingFactory.create(price=500000)
    url = urls.reverse('search')
    resp = client.get(url, {
        'price': 600000
    })
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_is_saved_for_authenicated_user(client, listing, authenticated_user):
    url = urls.reverse('search')
    resp = client.get(url)
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200
    assert Search.objects.count() == 1


def test_last_10_searches_are_saved_for_authenticated_user(client, authenticated_user):
    for n in range(20):
        listing = ListingFactory.create(title=f'listing{n}')
        url = urls.reverse('search')
        resp = client.get(url)
        assert b'No listings found' not in resp.content
        assert resp.status_code == 200
    assert Search.objects.count() == 10

