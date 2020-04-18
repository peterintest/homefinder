import factory
from datetime import datetime
from staff.models import Staff

class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    name = 'David Smith'
    job_title = 'Estate Agent'
    phone = '01234567891'
    email = 'agent@test.com'
    photo = factory.django.ImageField()
    start_date = factory.LazyFunction(datetime.now)
