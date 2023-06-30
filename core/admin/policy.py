from django.contrib import admin
from core.models.policy import Policy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "modified")
