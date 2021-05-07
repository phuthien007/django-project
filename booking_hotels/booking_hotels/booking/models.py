from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# model category room
class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images/categories', default='')
    price_randian = models.FloatField(default=0)
    def __str__(self):
        return self.name

# model room
class Rooms(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey('Categories',on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    status = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images/rooms')

    def __str__(self):
        return self.name


# model signup user
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username


# model book a room
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    number_adults = models.IntegerField(default=0)
    number_children = models.IntegerField(default=0)
    arival_date = models.DateField()
    departure_date = models.DateField()