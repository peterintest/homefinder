import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test___str__():
    name = 'David Jones'
    contact = mixer.blend('contacts.Contact', name=name)
    assert contact.__str__() == name
    assert str(contact) == name
