from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^bookings/$', views.BookingListView.as_view(), name='booking_all'),
    url(r'^bookings/(?P<id>[\w\-]+)/$', views.BookingDetailView.as_view(), name='booking_detail'),
    url(r'^dates/$', views.DateListView.as_view(), name='date_all'),
    url(r'^dates/(?P<date>[\w.@+-]+)/$', views.DateDetailView.as_view(), name='date'),
]
