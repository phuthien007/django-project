"""NotesSahringSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('login_user/', login_user, name='login'),
    path('login_admin/', login_admin, name='login_admin'),
    path('signup/', sign_up1, name= 'signup'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('upload_notes/', upload_notes, name= 'upload_notes'),
    path('view_mynotes/', view_mynotes, name= 'view_mynotes'),
    path('delete_notes/<int:id>', delete_notes, name= 'delete_notes'),
    path('delete_notes_admin/<int:id>', delete_notes_admin, name= 'delete_notes_admin'),
    path('view_users/', view_users, name= 'view_users'),
    path('delete_users/<int:id>', delete_user, name= 'delete_user'),
    path('pending_notes/', pending_notes, name= 'pending_notes'),
    path('accept_notes/', accept_notes, name= 'accept_notes'),
    path('reject_notes/', reject_notes, name= 'reject_notes'),
    path('all_notes/', all_notes, name= 'all_notes'),
    path('assign_notes/<int:id>', assign_notes, name= 'assign_notes'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
