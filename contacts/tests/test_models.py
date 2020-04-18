import pytest
from .factories import ContactFactory


def test___str__():
    contact = ContactFactory.build()
    assert contact.__str__() == contact.name
    assert str(contact) == contact.name
