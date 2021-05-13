from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

class AdminBooking(admin.ModelAdmin):
    list_display = [ "user",'room']


admin.site.register(Room)
admin.site.register(Signup)
admin.site.register(Categories)
admin.site.register(Booking,AdminBooking)
admin.site.register(Comment)
admin.site.register(Service)
admin.site.register(Category_service)
admin.site.register(Voucher)