import factory
from services.models import Service


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = 'Independent mortgage brokerage'
