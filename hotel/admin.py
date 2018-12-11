from django.contrib import admin
from .models import Hotel, Room_type, Room, Reservation, Reserved_room
#Profile
# Register your models here.
myModels = [Hotel, Room_type, Room, Reservation, Reserved_room]
admin.site.register(myModels)
