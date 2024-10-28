from django.contrib import admin
from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ("id", "vehicle", "driver", "expense_threshold", "total_expense")
    list_editable = ("expense_threshold",)  # Enable inline editing of thresholds

admin.site.register(Trip, TripAdmin)
