from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from datetime import date, datetime


# Create your views here.
# url home page


def index(request):
    category_lst = Categories.objects.all()
    comments = Comment.objects.order_by('-create_date')[:5]
    return render(request, 'index.html',{"categories": category_lst, "comments":comments})


# list category room
@login_required(login_url='/login_user/')
def category_room_list(request):
    Category1 = Categories.objects.get(name='Double Room')
    Category2 = Categories.objects.get(name='Double Room Luxury')
    Category3 = Categories.objects.get(name='Single Room')
    Category4 = Categories.objects.get(name='Suite Room')
    service1 = Category_service.objects.filter( category = Category1 )
    service2 = Category_service.objects.filter( category = Category2 )
    service3 = Category_service.objects.filter(category=Category3)
    service4 = Category_service.objects.filter(category=Category4)
    category_lst = Categories.objects.all()
    return render(request, 'category_room_list.html', {"categories": category_lst, "ser1": service1,"ser2": service2,"ser3": service3,"ser4": service4})


# list double room
@login_required(login_url='/login_user/')
def double_room_list(request):

    Category = Categories.objects.get(name='Double Room')
    service1 = Category_service.objects.filter(category=Category)
    double_lst = Category.room_set.all()
    double_room=[]
    for room in double_lst:
        c = 0
        booking= Booking.objects.filter(room = room)
        for b in booking:
            if b.departure_date >= date.today() and b.arival_date <= date.today():
                c+=1
        if c == 0:
            double_room.append(room)


    comments = Comment.objects.filter(category = Category).order_by('-create_date')[:5]
    return render(request, 'detail_room/room_list.html',
                  {"double_room_list": double_room, "Category": Category.name, "ser": service1, "comments": comments})


# list double luxury room
@login_required(login_url='/login_user/')
def double_room_luxury_list(request):
    Category = Categories.objects.get(name='Double Room Luxury')
    service1 = Category_service.objects.filter(category=Category)
    double_lst = Category.room_set.all()
    double_room_luxury = []
    for room in double_lst:
        c = 0
        booking = Booking.objects.filter(room=room)
        for b in booking:
            if b.departure_date >= date.today() and b.arival_date <= date.today():
                c += 1
        if c == 0:
            double_room_luxury.append(room)
    comments = Comment.objects.filter(category=Category).order_by('-create_date')[:5]
    return render(request, 'detail_room/room_list.html',
                  {"double_room_list": double_room_luxury, "Category": Category.name, "ser": service1, "comments": comments})


# list single room
@login_required(login_url='/login_user/')
def single_room_list(request):
    Category = Categories.objects.get(name='Single Room')
    service1 = Category_service.objects.filter(category=Category)
    double_lst = Category.room_set.all()
    single_room = []
    for room in double_lst:
        c = 0
        booking = Booking.objects.filter(room=room)
        for b in booking:
            if b.departure_date >= date.today() and b.arival_date <= date.today():
                c += 1
        if c == 0:
            single_room.append(room)
    comments = Comment.objects.filter(category=Category).order_by('-create_date')[:5]
    return render(request, 'detail_room/room_list.html',
                  {"double_room_list": single_room, "Category": Category.name, "ser": service1, "comments": comments})


# list suite room
@login_required(login_url='/login_user/')
def suite_room_list(request):
    Category = Categories.objects.get(name='Suite Room')
    service1 = Category_service.objects.filter(category=Category)
    double_lst = Category.room_set.all()
    suite_room = []
    for room in double_lst:
        c = 0
        booking = Booking.objects.filter(room=room)
        for b in booking:
            if b.departure_date >= date.today() and b.arival_date <= date.today():
                c += 1
        if c == 0:
            suite_room.append(room)
    comments = Comment.objects.filter(category=Category).order_by('-create_date')[:5]
    return render(request, 'detail_room/room_list.html',
                  {"double_room_list": suite_room, "Category": Category.name, "ser":service1, "comments": comments})


# to login
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    error = ''
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(username=email, password=pwd)
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
    return render(request, 'user/login_user.html', {'error': error, 'next_page': next_page})


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
    data = Signup.objects.filter(user=request.user).first()
    return render(request, 'user/profile.html', {'data': data})


# to change password user
@login_required(login_url='/login_user/')
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = ""
    if request.method == 'POST':
        o_p = request.POST['o-pwd']
        n_p = request.POST['n-pwd']
        c_p = request.POST['c-pwd']
        u = User.objects.get(username__exact=request.user.username)
        if not check_password(o_p, u.password):
            error = "yes"
        elif c_p == n_p:
            u.password = make_password(n_p)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {"error": error}
    return render(request, 'user/changepassword.html', d)


# to show your room booking
@login_required(login_url='/login_user/')
def my_room(request):
    my_room = Booking.objects.filter(user=request.user)
    return render(request, 'user/my_rooms.html', {'room_list': my_room,"error":"no"})

# format datetime booking
def format_date(datetime):
    datetime = datetime.split()
    day = datetime[1] if datetime[1] > '10' else '0' + datetime[1]
    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Now': '11', 'Dec': '12'}
    year = date.today().year
    return '-'.join([str(year), month[datetime[0]], day])


# to booking a room
@login_required(login_url='/login_user/')
def booking_room(request):
    if request.method == 'POST':
        data = request.POST['data']
        check_in_date = request.POST['check_in']
        check_out_date = request.POST['check_out']
        adults = (request.POST['adults'])
        children = (request.POST['children'])
        voucher_code = request.POST['voucher_code']
        try:
            check_in_date = format_date(check_in_date)
            check_out_date = format_date(check_out_date)
        except:
            my_room = Booking.objects.filter(user=request.user)
            return render(request, 'user/my_rooms.html', {'room_list': my_room})
        adults = 0 if (adults == '') else int(adults)
        children = 0 if (children == '') else int(children)
        my_room = Booking.objects.filter(user=request.user)
        voucher = Voucher.objects.filter(code = voucher_code).first()
        if voucher != ' ' and voucher is not None:
            if voucher.qty > 0:
                voucher.qty-=1
                voucher.save()
            elif voucher.create_date > date.today():
                voucher_code = ' '
            elif voucher.end_date < date.today():
                voucher_code = ' '
            else:
                voucher_code = ' '
        else:
            voucher_code = ' '

        if data is not None and adults != 0  and (adults + children) <=10 :
            data = data.split()
            for item in data:
                room = Room.objects.filter(name=item).first()
                o_room = Booking.objects.filter(user = request.user, room = room).first()
                booking = Booking.objects.filter(room=room)
                for b in booking:
                    if (str(b.departure_date) > check_in_date and str(b.arival_date) < check_in_date) or \
                            (str(b.departure_date) > check_out_date and str(b.arival_date) < check_out_date) or\
                            (str(b.arival_date) > check_in_date and str(b.departure_date) < check_out_date):
                        return render(request, 'user/my_rooms.html', {'room_list': my_room,"error":"yes"})
                if o_room is None:
                    room.status = 2
                    room.save()
                    a = Booking.objects.create(room=room, user=request.user, number_adults=adults, number_children=children,
                                           arival_date=check_in_date, departure_date=check_out_date, voucher_code = voucher_code)
                    a.save()
        my_room = Booking.objects.filter(user=request.user)
        return render(request, 'user/my_rooms.html', {'room_list': my_room,"error":"no"})


@login_required(login_url='/login_user/')
def create_comment(request):
    if request.method == 'POST':
        room_type_review = request.POST['room_type_review']
        position_review = request.POST['position_review']
        comfort_review = request.POST['comfort_review']
        price_review = request.POST['price_review']
        quality_review = request.POST['quality_review']
        review_text = request.POST['review_text']
        evals = "Position: " + position_review + ' Comfort: ' + comfort_review + ' Price: ' +  price_review + ' Quality: ' +  quality_review
        # print(evals, len(evals))
        category = Categories.objects.filter(name = room_type_review).first()
        # print(category, room_type_review)
        if category is None or category == '':
            # print("errror1")
            return redirect('category_room_list')
        if room_type_review != '':
            tmp = Comment.objects.create(category = category, user = request.user, evaluation = evals, comment = review_text)
            url_name = '_'.join([ i.lower() for i in room_type_review.split() ])+"_list"
            return  redirect(url_name)
        # print("error2")
    return redirect('category_room_list')

# cancel booking

def cancel_booking(request):
    if request.method == 'POST':
        room_name = request.POST['cancel_booking']
        room = Room.objects.filter(name = room_name).first()
        b= Booking.objects.filter(room = room).first()
        try:
            b.delete()
            room.status = 0
        except:
            pass
    return  redirect('my_room')



# admintration

# show room
def admin_room(request):
    if not request.user.is_staff:
        return redirect('/admin')
    rooms = Room.objects.all()
    return render(request,'admin/admin_room.html',{"rooms":rooms})


# delete room
def admin_room_delete(request,id):
    if not request.user.is_staff:
        return redirect('/admin')
    try:
        room = Room.objects.get(pk=id)
        room.delete()
    except:
        pass
    return  redirect('admin_room')


# accept booking
def assign_rooms(request,id):
    if not request.user.is_staff:
        return redirect('login_user')

    rooms= Room.objects.get(id= id)
    error = ""
    if request.method == 'POST':
        s = request.POST['status']
        try:
            rooms.status = 1 if s == 'Accept' else 0
            rooms.save()
            error= "no"
        except:
            error = "yes"
    d= {'notes':rooms,'error':error}
    return render(request,'admin/assign_status.html',d)

# show booking
def admin_booking(request):
    if not request.user.is_staff:
        return redirect('/admin')
    b = Booking.objects.all()
    return render(request,'admin/admin_booking.html',{"rooms":b})

# delete booking
def admin_booking_room_delete(request,id):
    if not request.user.is_staff:
        return redirect('/admin')
    try:
        room = Booking.objects.get(pk=id)
        room.room.status = 0
        room.room.save()
        room.delete()
    except:
        pass
    return redirect('admin_booking')

def total_bill(request,id):
    if not request.user.is_staff:
        return redirect('/admin')
    b1 = Booking.objects.filter(id = id).first()
    a = int(str(b1.departure_date - b1.arival_date).split()[0])
    if( a<0 ):
        return redirect('admin_booking')
    else:
        user = b1.user
        room = b1.room
        total_price = a * int(room.price)
        voucher = Voucher.objects.filter(code = b1.voucher_code).first()
        if voucher != ' ' and voucher is not None:
            total_price-= voucher.discount * a * int(room.price)
        return render(request, 'admin/total_bill.html',{"user":user,"room":room,"total_price":total_price})

def accept_bill(request):
    if not request.user.is_staff:
        return redirect('/admin')
    if request.method == 'POST':
        room = Room.objects.filter(name = request.POST['room_name']).first()
        user = User.objects.filter(username=request.POST['username']).first()
        b = Booking.objects.filter(room = room, user= user).first()
        b.delete()
        room.status = 0
        room.save()
        return redirect(admin_booking)



EMAIL_HOST_USER = 'phailamsaonana@gmail.com'
def send_notification(request):
    if request.method == 'POST':
        first_name = (request.POST['name_contact'])
        last_name = (request.POST['lastname_contact'])
        email  = request.POST['email_contact']
        phone_contact = request.POST['phone_contact']
        message_contact = request.POST['message_contact']
        mgs = f'''
            From:  {email} 
            Fullname: {first_name} {last_name}
            Phone: {phone_contact}
            Send Message: {message_contact}
        '''
        send_mail("A new Customer",
                  "Your Message Sent", EMAIL_HOST_USER, [email], fail_silently=False)
        send_mail("A new Customer",
                  mgs, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False)
        return render(request, 'success.html')
