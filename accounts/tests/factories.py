import factory
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'Bob'
    last_name = 'Jones'
    username='username1'
    password=factory.PostGenerationMethodCall('set_password', 'password1')
    email='email@test.com'
    is_staff = False
