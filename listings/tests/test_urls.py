from django import urls


def test_listings_url():
    url = urls.reverse('index')
    assert urls.resolve(url).view_name == 'index'


def test_listing_url():
    url = urls.reverse('listing', kwargs={'listing_id': 1})
    assert urls.resolve(url).view_name == 'listing'


def test_search_url():
    url = urls.reverse('search')
    assert urls.resolve(url).view_name == 'search'
