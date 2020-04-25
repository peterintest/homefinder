from django import urls
from contacts.models import Contact
import pytest

pytestmark = pytest.mark.unittest

def test_enquiry(client, listing):
    url = urls.reverse('contact')
    resp = client.post(url, {
        'listing': 'Listing 1',
        'listing_id': listing.id,
        'name': 'David Jones',
        'email':'test@example.com',
        'phone': '012345678912',
        'message': 'This is a test message'
    })
    assert resp.status_code == 302
    assert resp.url == urls.reverse('listing', kwargs={'listing_id': listing.id})
    assert Contact.objects.filter(message='This is a test message').exists()
    assert Contact.objects.count() == 1
