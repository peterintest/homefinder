from django.contrib import admin

from .models import Listing, Search

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'city', 'staff')
    list_display_links = ('id', 'title')
    list_filter = ('staff', 'city')
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'description', 'city', 'county', 'postcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'search_date', 'user', 'keywords', 'bedrooms', 'max_price')
    list_display_links = ('id', 'keywords')
    list_filter = ('user',)
    list_per_page = 25

admin.site.register(Search, SearchAdmin)
