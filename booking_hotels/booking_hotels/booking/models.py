from datetime import date

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# model category room
from django.db.models import UniqueConstraint


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images/categories', default='')
    price_randian = models.FloatField(default=0)

    def __str__(self):
        return self.name


# model room
class Room(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
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
        return self.user.first_name + ' ' + self.user.last_name


# model book a room
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_adults = models.IntegerField(default=0)
    number_children = models.IntegerField(default=0)
    arival_date = models.DateField()
    departure_date = models.DateField()
    voucher_code = models.CharField(max_length=20, default=' ', null=True)
    UniqueConstraint(fields=['user', 'room'], name='unique_user_booking')


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + '-' + self.room.name


# model service in a category

class Service(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/service')
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category_service(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete= models.CASCADE)

    def __str__(self):
        return self.category.name + ' '  + self.service.name

class Comment(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation = models.CharField(max_length=200, default='')
    comment = models.CharField( max_length=200 , null=False, default="good")
    create_date = models.DateField( default= date.today())

    def __str__(self):
        return self.user.username + ' comment: ' + self.category.name

class Voucher(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    discount = models.FloatField(default=0)
    qty = models.IntegerField(default=0)
    description = models.CharField(max_length=100, null=True)
    create_date = models.DateField(default= date.today())
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.name + self.qty
