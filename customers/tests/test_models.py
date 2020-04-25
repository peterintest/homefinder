import pytest
from .factories import CustomerFactory

pytestmark = pytest.mark.unittest

def test___str__():
    customer = CustomerFactory.build()
    assert customer.__str__() == customer.name
    assert str(customer) == customer.name
