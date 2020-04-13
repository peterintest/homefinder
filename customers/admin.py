from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'postcode', 'city', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address', )
    list_per_page = 25

admin.site.register(Customer, CustomerAdmin)
