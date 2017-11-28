from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^bookings/$', views.BookingListView.as_view(), name='booking_all'),
    url(r'^bookings/(?P<id>[\w\-]+)/$', views.BookingDetailView.as_view(), name='booking_detail')
]
