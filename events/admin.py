from django.contrib import admin

from .models import Event

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'date', 'organiser')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'location', 'date', 'organiser')
    list_per_page = 25

admin.site.register(Event, EventsAdmin)
