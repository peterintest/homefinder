import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test___str__():
    title = '33 Sesame street'
    listing = mixer.blend('listings.Listing', title=title)
    assert listing.__str__() == title
    assert str(listing) == title
