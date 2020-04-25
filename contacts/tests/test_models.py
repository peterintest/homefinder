import pytest
from .factories import ContactFactory

pytestmark = pytest.mark.unittest

def test___str__():
    contact = ContactFactory.build()
    assert contact.__str__() == contact.name
    assert str(contact) == contact.name
