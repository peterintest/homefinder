import factory
from django.utils import timezone
from contacts.models import Contact

class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    listing = 'Listing 1'
    listing_id = 1
    name = 'David Jones'
    email = 'test@example.com'
    phone = '012345678912'
    message = 'This is a test message'
    contact_date = timezone.now
