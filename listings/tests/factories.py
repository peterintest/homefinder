import factory
from django.utils import timezone
from listings.models import Listing

class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listing

    staff = factory.SubFactory('staff.tests.factories.StaffFactory')
    title = '1 Lucerne Close'
    address = '1 Lucerne Close'
    city = 'Cambridge'
    county = 'Cambridgeshire'
    postcode = 'CB1 2AB'
    description = 'A spacious three bedroom property'
    price = 375000
    bedrooms = 3
    bathrooms = 1
    livingrooms = 2
    garage = 1
    photo_main = factory.django.ImageField()
    photo_1 = factory.django.ImageField()
    photo_2 = factory.django.ImageField()
    photo_3 = factory.django.ImageField()
    photo_4 = factory.django.ImageField()
    photo_5 = factory.django.ImageField()
    photo_6 = factory.django.ImageField()
    is_published = True
    creation_date = timezone.now()
