from django.contrib import admin
from core.models.event import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
