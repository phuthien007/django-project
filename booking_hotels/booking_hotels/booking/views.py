from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from  .models import *
from datetime import date
# Create your views here.
# url home page
def index(request):
    return render(request, 'index.html')

# list category room
@login_required(login_url='/login_user/')
def category_room_list(request):
    url_login='/login_user'
    category_lst= Categories.objects.all()
    return render(request, 'category_room_list.html',{"categories": category_lst})

# list double room
@login_required(login_url='/login_user/')
def double_room_list(request):
    Category = Categories.objects.get(name= 'Double Room')
    double_lst = Category.rooms_set.filter(status = 0)
    return render(request, 'detail_room/room_list.html', {"double_room_list": double_lst,"Category":Category.name})

# list double luxury room
@login_required(login_url='/login_user/')
def double_room_luxury_list(request):
    Category = Categories.objects.get(name='Double Room Luxury')
    double_lst = Category.rooms_set.filter(status=0)
    return render(request, 'detail_room/room_list.html',
                  {"double_room_list": double_lst, "Category": Category.name})

# list single room
@login_required(login_url='/login_user/')
def single_room_list(request):
    Category = Categories.objects.get(name='Single Room')
    double_lst = Category.rooms_set.filter(status=0)
    return render(request, 'detail_room/room_list.html',{"double_room_list": double_lst, "Category": Category.name})

# list suite room
@login_required(login_url='/login_user/')
def suite_room_list(request):
    Category = Categories.objects.get(name='Suite Room')
    double_lst = Category.rooms_set.filter(status=0)
    return render(request, 'detail_room/room_list.html', {"double_room_list": double_lst, "Category": Category.name})


# to login
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    error = ''
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(username = email, password = pwd)
        try:
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    try:
        next_page = request.GET['next']
    except:
        next_page = ''
    return render(request,'user/login_user.html',{'error':error,'next_page':next_page})

# to logout
def Logout(request):
    logout(request)
    return redirect('login_user')


# to signup
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    error = ""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['pwd']
        try:
            user = User.objects.create_user(username=email, password=password, first_name=first_name,
                                            last_name=last_name)
            Signup.objects.create(user=user, contact=contact)
            error = 'no'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'user/sign_up.html', d)


# show profile user
@login_required(login_url='/login_user/')
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    data = Signup.objects.filter(user = request.user).first()
    return render(request,'user/profile.html',{'data':data})


# to change password user
@login_required(login_url='/login_user/')
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    if request.method =='POST':
        o_p= request.POST['o-pwd']
        n_p= request.POST['n-pwd']
        c_p= request.POST['c-pwd']
        u = User.objects.get(username__exact= request.user.username)
        if not check_password(o_p,u.password):
            error="yes"
        elif c_p==n_p:
            u.password = make_password(n_p)
            u.save()
            error="no"
        else:
            error="yes"
    d= {"error":error}
    return render(request,'user/changepassword.html',d)


# to show your room booking
@login_required(login_url='/login_user/')
def my_room(request):
    my_room = Booking.objects.filter(user = request.user)
    print(my_room)
    return  render(request,'user/my_rooms.html',{'room_list':my_room})

# format datetime booking
def format_date(date):
    pass


# to booking a room
@login_required(login_url='/login_user/')
def booking_room(request):
    if request.method == 'POST':
        print((request.POST['check_in']))
        print(date.today())
        my_room = Booking.objects.filter(user=request.user)
        return render(request,'user/my_rooms.html',{'room_list':my_room})
