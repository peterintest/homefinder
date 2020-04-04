from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
def test___str__():
    name = 'David Jones'
    listing = mixer.blend('staff.Staff', name=name)
    assert listing.__str__() == name
    assert str(listing) == name
