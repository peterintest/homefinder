import pytest
from .factories import ServiceFactory


def test___str__():
    service = ServiceFactory.build()
    assert service.__str__() == service.name
    assert str(service) == service.name
