import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test___str__():
    name = 'Independent mortgage brokerage'
    service = mixer.blend('services.Service', name=name)
    assert service.__str__() == name
    assert str(service) == name
