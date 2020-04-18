import factory
from datetime import datetime
from events.models import Event


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = 'Education Property & Development Conference'
    description = 'Popular property conference'
    location = 'London conference centre'
    date = factory.LazyFunction(datetime.now)
    organiser = factory.SubFactory('staff.tests.factories.StaffFactory')
