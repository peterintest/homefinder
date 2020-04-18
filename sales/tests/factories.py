import factory
from datetime import datetime
from sales.models import Purchase, Sale

class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    customer = factory.SubFactory('customers.tests.factories.CustomerFactory')
    listing = factory.SubFactory('listings.tests.factories.ListingFactory')
    agent = factory.SubFactory('staff.tests.factories.StaffFactory')
    amount = 500000
    completion_date = factory.LazyFunction(datetime.now)


class SaleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sale

    customer = factory.SubFactory('customers.tests.factories.CustomerFactory')
    listing = factory.SubFactory('listings.tests.factories.ListingFactory')
    agent = factory.SubFactory('staff.tests.factories.StaffFactory')
    amount = 500000
    completion_date = factory.LazyFunction(datetime.now)
