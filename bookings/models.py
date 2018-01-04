# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from .utils.validators import PHONE_REGEX


class Date(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True, null=False, blank=False)


class Time(models.Model):
    AVAILABLE_TIMESLOTS = (
        ('9:00 to 9:30', '9:00 to 9:30'),
        ('10:00 to 10:30', '10:00 to 10:30'),
        ('11:00 to 11:30', '11:00 to 11:30'),
    )

    AVAILABILITY_STATUS = (
        ('available', 'Available'),
        ('on_process', 'On Booking Process'),
        ('booked', 'Booked'),
    )

    time_slot = models.CharField(choices=AVAILABLE_TIMESLOTS, max_length=32, null=False, blank=False)
    date_id = models.ForeignKey('Date', null=False, blank=False, on_delete=models.CASCADE, related_name='times')
    availability_status = models.CharField(choices=AVAILABILITY_STATUS, max_length=55, null=False, blank=False)

    class Meta:
        unique_together = (('time_slot', 'date_id'),)


class Booking(models.Model):
    BOOKING_STATUSES = (
        ('new', 'New'),
        ('on_process', 'On Process'),
        ('confirmed', 'Confirmed'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    company_name = models.CharField(max_length=255, null=False, blank=False)
    meetup_location = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(choices=BOOKING_STATUSES, max_length=10, default='new')
    date = models.DateField(null=False, blank=False)
    time_slot = models.CharField(max_length=255)

    class Meta:
        unique_together = (('time_slot', 'date'),)

    def __unicode__(self):
        return self.id
