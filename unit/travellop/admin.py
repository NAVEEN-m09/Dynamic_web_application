from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "appointment_date", "appointment_time", "created_at")
    list_filter = ("appointment_date", "created_at")
    search_fields = ("name", "phone", "email")
