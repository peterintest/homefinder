from django.urls import reverse, resolve
import pytest

pytestmark = pytest.mark.unittest

def test_contact_url():
    path = reverse('contact')
    assert resolve(path).view_name == 'contact'
