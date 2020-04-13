import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test___str__():
    name = 'David Smith'
    customer = mixer.blend('customers.Customer', name=name)
    assert customer.__str__() == name
    assert str(customer) == name
