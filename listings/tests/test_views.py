from django import urls
from django.contrib.auth.models import AnonymousUser
from listings.views import index, listing, search, Search
from mixer.backend.django import mixer
import pytest


@pytest.fixture
def property_listing(db):
    return mixer.blend('listings.Listing')


def test_listings(client, property_listing):
    listing_id = property_listing.pk
    url = urls.reverse('listings')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Our Properties' in resp.content


def test_listing_details(client, property_listing):
    listing_id = property_listing.pk
    url = urls.reverse('listing', kwargs={'listing_id': listing_id})
    resp = client.get(url)
    assert resp.status_code == 200


def test_search_no_listings(client, property_listing):
    url = urls.reverse('search')
    resp = client.get(url)
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_by_keyword(client, property_listing):
    mixer.blend('listings.Listing', city="Cambridge")
    url = urls.reverse('search')
    resp = client.get(url, {
        'keywords': 'Cambridge'
    })
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_filter_by_num_bedrooms(client, db):
    mixer.blend('listings.Listing', bedrooms=3)
    url = urls.reverse('search')
    resp = client.get(url, {
        'bedrooms': 3
    })
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_filter_by_max_price(client, db):
    mixer.blend('listings.Listing', price=500000)
    url = urls.reverse('search')
    resp = client.get(url, {
        'price': 600000
    })
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200


def test_search_is_saved_for_authenicated_user(client, db, authenticated_user):
    mixer.blend('listings.Listing')
    url = urls.reverse('search')
    resp = client.get(url)
    assert b'No listings found' not in resp.content
    assert resp.status_code == 200
    assert Search.objects.count() == 1


def test_last_10_searches_are_saved_for_authenicated_user(client, db, authenticated_user):
    for n in range(20):
        mixer.blend('listings.Listing')
        url = urls.reverse('search')
        resp = client.get(url)
        assert b'No listings found' not in resp.content
        assert resp.status_code == 200
    assert Search.objects.count() == 10

