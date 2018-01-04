from rest_framework import generics
from ..models import Booking
from ..models import Date
from ..models import Time
from .serializers import BookingSerializer
from .serializers import DateSerializer
from .serializers import TimeSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class BookingListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookingDetailView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class TimeListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TimeDetailView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DateListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DateDetailView(generics.RetrieveAPIView):
    lookup_field = "date"
    queryset = Date.objects.all()
    serializer_class = DateSerializer
