from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('offer/', views.offer, name='offer'),
    path('booking/', views.bookRoom, name='bookRoom'),
    path('bookSuccess/<int:pk>', views.bookSuccess, name='bookSuccess')
]

#path('signUp/', views.signUp, name='signUp'),