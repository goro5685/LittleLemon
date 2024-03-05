from django.contrib import admin
from django.urls import path
from .views import index, about, menu, menu_item, bookings, Book

urlpatterns = [
    path('', index , name='home'),
    path('about/', about , name='about'),
    path('menu/', menu , name='menu'),
    path('menu-item/<int:pk>/', menu_item, name='menu-detail'),
    path('book/', Book.as_view(), name='book'),
    path('bookings/', bookings, name='bookings'),
]