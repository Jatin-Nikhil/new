from django.contrib import admin
from .models import Hotel, Room_type, Room, Profile, Reservation, Reserved_room

# Register your models here.
myModels = [Hotel, Room_type, Room, Profile, Reservation, Reserved_room]
admin.site.register(myModels)
