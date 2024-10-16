from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('crud/', views.hotel_index, name='crud'),
    path("crud/create", views.hotel_create, name="hotel_create"),
    path("crud/update/<int:hotel_id>", views.hotel_update, name="hotel_update"),
    path("crud/delete/<int:hotel_id>", views.hotel_delete, name="hotel_delete"),
    path('hotels/', views.booking_index, name='booking_index'),
    path('book/<int:hotel_id>/', views.booking_view, name='booking_view'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
