from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25
    readonly_fields = [
        'name',
        'listing',
        'listing_id',
        'name',
        'email',
        'phone',
        'message',
        'contact_date'
    ]

admin.site.register(Contact, ContactAdmin)
