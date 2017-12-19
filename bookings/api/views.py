from rest_framework import generics
from ..models import Booking
from ..models import Date
from .serializers import BookingSerializer
from .serializers import DateSerializer
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


class DateListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DateDetailView(generics.RetrieveAPIView):
    lookup_field = "date"
    queryset = Date.objects.all()
    serializer_class = DateSerializer
