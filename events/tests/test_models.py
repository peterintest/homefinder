import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
def test___str__():
    title = 'Education Property & Development Conference'
    event = mixer.blend('events.Event', title=title)
    assert event.__str__() == title
    assert str(event) == title
