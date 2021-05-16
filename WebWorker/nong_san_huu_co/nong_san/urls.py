from django.urls import path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # dùng để đăng nhập
    path('api/dangnhap', obtain_auth_token, name='dangnhap'),
    # dùng để đổi mk
    path('api/doimk', change_password, name='doimk'),
    # dùng để đăng kí
    path('api/dangki', signup, name='signup'),
    # dùng gửi báo cáo
    path('api/gui_bao_cao', gui_bao_cao, name='gui_bao_cao'),
    # dùng xem ds công việc
    path('api/ds_cong_viec',ds_cong_viec,name= 'ds_cong_viec'),
]
