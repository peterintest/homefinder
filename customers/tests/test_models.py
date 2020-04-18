import pytest
from .factories import CustomerFactory


def test___str__():
    customer = CustomerFactory.build()
    assert customer.__str__() == customer.name
    assert str(customer) == customer.name
