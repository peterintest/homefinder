from django.contrib import admin

from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'start_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Staff, StaffAdmin)
