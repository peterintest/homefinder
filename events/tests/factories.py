import factory
from django.utils import timezone
from events.models import Event


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = 'Education Property & Development Conference'
    description = 'Popular property conference'
    location = 'London conference centre'
    date = timezone.now
    organiser = factory.SubFactory('staff.tests.factories.StaffFactory')
