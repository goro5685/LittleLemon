from django.urls import path
from .views import BookingView, MenuItemView, SingleBookingView, SingleMenuItemView

app_name ='api'
urlpatterns = [
    path('menu-items', MenuItemView.as_view(), name='menu'),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view(), name='menu-detial'),
    path('bookings', BookingView.as_view(), name='bookings'),
    path('bookings/<int:pk>', SingleBookingView.as_view(), name='booking-detial'),
]
