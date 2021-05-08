from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', TemplateView.as_view(template_name='about.html')),
    path('contact', TemplateView.as_view(template_name='contacts.html')),
    path('support', TemplateView.as_view(template_name='support.html')),
    path('category_room_list/', category_room_list, name='category_room_list'),
    path('category_room_list/double_room_list/', double_room_list, name='double_room_list'),
    path('category_room_list/double_room_luxury_list/', double_room_luxury_list, name='double_room_luxury_list'),
    path('category_room_list/single_room_list/', single_room_list, name='single_room_list'),
    path('category_room_list/suite_room_list/', suite_room_list, name='suite_room_list'),
    path('login_user/', login_user, name='login_user'),
    path('logout/', Logout, name='logout'),
    path('sign_up/', sign_up, name='sign_up'),
    path('my_profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('my_rooms/', my_room, name='my_room'),
    path('booking_room/', booking_room, name='booking_room'),
    path('create_comment/', create_comment, name='create_comment'),
    path('cancel_booking/', cancel_booking, name='cancel_booking'),
    # adminstration
    path('admin_room/', admin_room, name='admin_room'),
    path('admin_room/delete/<int:id>', admin_room_delete, name='admin_room_delete'),
    path('assign_rooms/<int:id>', assign_rooms, name='assign_rooms'),
    path('admin_booking/', admin_booking, name='admin_booking'),
    path('admin_booking/delete/<int:id>', admin_booking_room_delete, name='admin_booking_room_delete'),

]
