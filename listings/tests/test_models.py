import pytest
from .factories import ListingFactory


@pytest.mark.django_db
def test___str__(listing):
    assert listing.__str__() == listing.title
    assert str(listing) == listing.title
