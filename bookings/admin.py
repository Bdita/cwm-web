# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Booking
from .models import Date
from .models import Time


class TimeAdmin(admin.TabularInline):
    model = Time


class DateAdmin(admin.ModelAdmin):
    inlines = [TimeAdmin]
    list_display = ['id', 'date']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'modified_at', 'name', 'email', 'description', 'phone', 'company_name', 'status', 'date', 'time_slot', 'meetup_location']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Date, DateAdmin)
