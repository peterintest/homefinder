import pytest
from .factories import EventFactory

pytestmark = pytest.mark.unittest

def test___str__():
    event = EventFactory.build()
    assert event.__str__() == event.title
    assert str(event) == event.title
