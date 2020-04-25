import pytest
from .factories import ServiceFactory

pytestmark = pytest.mark.unittest

def test___str__():
    service = ServiceFactory.build()
    assert service.__str__() == service.name
    assert str(service) == service.name
