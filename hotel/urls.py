from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('offer/', views.offer, name='offer'),
    path('booking/', views.book_room, name='bookRoom'),
    path('bookSuccess/<int:pk>', views.book_success, name='bookSuccess'),
    path('signUp/', views.sign_up, name='signUp'),
    path('bookings/', views.my_bookings, name='bookings'),
]

