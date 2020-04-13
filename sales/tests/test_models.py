import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_sale___str__():
    title = '33 Sesame street'
    listing = mixer.blend('listings.Listing', title=title)
    sale = mixer.blend('sales.Sale', listing=listing)
    assert sale.__str__() == title
    assert str(sale) == title


@pytest.mark.django_db
def test__purchase__str__():
    title = '33 Sesame street'
    listing = mixer.blend('listings.Listing', title=title)
    purchase = mixer.blend('sales.Purchase', listing=listing)
    assert purchase.__str__() == title
    assert str(purchase) == title