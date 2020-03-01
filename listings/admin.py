from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'city', 'staff')
    list_display_links = ('id', 'title')
    list_filter = ('staff', 'city')
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'description', 'city', 'county', 'postcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
