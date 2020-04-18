from .factories import StaffFactory
import pytest


def test___str__():
    staff = StaffFactory.build()
    assert staff.__str__() == staff.name
    assert str(staff) == staff.name
