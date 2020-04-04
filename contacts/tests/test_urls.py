from django.urls import reverse, resolve


def test_contact_url():
    path = reverse('contact')
    assert resolve(path).view_name == 'contact'
