from django.db import models
from django.utils import timezone
"""from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver"""
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    postCode = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 9)
    description = models.CharField(max_length = 700)
    email = models.CharField(max_length = 100) 

    def __str__(self):
        return 'Hotel: %s Adress: %s %s %s Contact: %s'%(self.name, self.city, self.street,
                                                         self.postCode, self.phone)

class Room_type(models.Model):
    typeID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    capacity = models.IntegerField()
    description = models.CharField(max_length = 500)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    hotelName = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    rented = models.BooleanField(default = False)
    roomType = models.ForeignKey(Room_type, on_delete = models.CASCADE)

    def __str__(self):
        return 'Room number: %d Room type: %d Room name: %s Hotel: %s Capacity: \
                %s Rented: %s Price: %d Description: %s'%(self.number, self.roomType.typeID, self.roomType.name, self.hotelName.name,
                                                            self.roomType.capacity, self.rented, self.roomType.price, self.roomType.description)

"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 9)
    email = models.EmailField()

    def __str__(self):
        return 'Nickname: %s Name: %s Surname: %s Phone: %s Email: %s'%(self.user, self.name, self.surname,
                                                                        self.phone, self.email)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""

class Reservation(models.Model):
    reservationID = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 9)
    email = models.EmailField()
    bookIn = models.DateField('Book in date', default = timezone.now)
    bookOut = models.DateField('Book out date', default = timezone.now)
    roomType = models.ForeignKey(Room_type, on_delete = models.CASCADE)

    def __str__(self):
        return 'Reservation: %d Guest: %s %s Type of Room: %s Book in: %s Book out: %s'%(self.reservationID, self.name, self.surname, 
                                                                                        self.roomType.name, self.bookIn, self.bookOut)

    def price(self):
        delta = self.bookOut - self.bookIn
        payment = self.roomType.price * (1 + delta.days)
        return payment


class Reserved_room(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete = models.CASCADE)
    room = models.OneToOneField(Room, on_delete = models.CASCADE)

    def __str__(self):
        guest = self.reservation.name + " " + self.reservation.surname
        return 'Reserved room: %d Reservation ID: %d From: %s \
                To: %s Guest: %s'%(self.room.number, self.reservation.reservationID, self.reservation.bookIn,
                                                self.reservation.bookOut, self.guest)
