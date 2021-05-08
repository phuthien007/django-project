from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

class AdminBooking(admin.ModelAdmin):
    list_display = [ "user",'room']


admin.site.register(Rooms)
admin.site.register(Signup)
admin.site.register(Categories)
admin.site.register(Booking,AdminBooking)
admin.site.register(Comments)
admin.site.register(service)