from rest_framework import serializers
from ..models import Booking
from ..models import Date
from ..models import Time


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'created_at', 'modified_at', 'name', 'email', 'description', 'phone', 'company_name', 'status', 'date', 'time_slot')


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'time_slot', 'date_id', 'availability_status')


class DateSerializer(serializers.ModelSerializer):
    times = TimeSerializer(many=True, read_only=True)

    class Meta:
        model = Date
        fields = ('id', 'date', 'times')
