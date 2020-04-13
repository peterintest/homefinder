from django.contrib import admin

from .models import Sale, Purchase

class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'agent', 'customer', 'amount', 'completion_date')
    list_display_links = ('id', 'listing')
    search_fields = ('listing', 'agent', 'customer', 'amount', 'completion_date')
    list_per_page = 25

admin.site.register(Sale, SalesAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'agent', 'customer', 'amount', 'completion_date')
    list_display_links = ('id', 'listing')
    search_fields = ('listing', 'agent', 'customer', 'amount', 'completion_date')
    list_per_page = 25

admin.site.register(Purchase, PurchaseAdmin)
