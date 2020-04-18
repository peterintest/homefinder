import pytest
from .factories import SaleFactory, PurchaseFactory


@pytest.mark.django_db
def test_sale___str__():
    title = '33 Sesame street'
    sale = SaleFactory.build(
        listing__title = title
    )
    assert sale.__str__() == title
    assert str(sale) == title


def test_purchase__str__():
    title = '33 Sesame street'
    purchase = PurchaseFactory.build(
        listing__title = title
    )
    assert purchase.__str__() == title
    assert str(purchase) == title