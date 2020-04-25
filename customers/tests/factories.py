import factory
from customers.models import Customer

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = 'James Smith'
    address = '1 Amazing Street'
    city = 'Cambridge'
    county = 'Cambridgeshire'
    postcode = 'CB1 2AB'
    email = 'customer@test.com'
    phone = '01234567891'
