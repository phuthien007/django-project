from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import date


# Create your views here.
def about(request):
    return render(request, "about.html")


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, 'contact.html')


def login_user(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'login.html',d)


def login_admin(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'login_admin.html',d)


def sign_up1(request):
    error=""
    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        contact= request.POST['contact']
        email= request.POST['email']
        password= request.POST['pwd']
        branch= request.POST['branch']
        role= request.POST['role']
        try:
            user= User.objects.create_user(username= email, password= password, first_name=first_name, last_name=last_name)
            Signup.objects.create(user=user, contact= contact, branch=branch, role=role)
            error='no'
        except:
            error='yes'
    d= {'error':error}
    return render(request, 'signup.html',d)


def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    p = Notes.objects.filter(status = 'pending' ).count()
    a = Notes.objects.filter(status = 'Accept' ).count()
    r = Notes.objects.filter(status = 'Reject' ).count()
    al = Notes.objects.all().count()
    return render(request, 'admin_home.html',{'p':p,'a':a,'r':r,'al':al})

def Logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    if not request.user.is_authenticated:
        return  redirect('login_user')
    user= User.objects.get(id= request.user.id)
    data = Signup.objects.get(user=user)
    d= {'data':data,'user':user}
    return  render(request,'profile.html',d)

def change_password(request): 
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    if request.method =='POST':
        o_p= request.POST['o-pwd']
        n_p= request.POST['n-pwd']
        c_p= request.POST['c-pwd']
        u = User.objects.get(username__exact= request.user.username)
        if u.password != o_p:
            error="yes"
        elif c_p==n_p:
            u.set_password(n_p)
            u.save()
            error="no"
        else:
            error="yes"
    d= {"error":error}
    return render(request,'changepassword.html',d)

def edit_profile(request):
    if not request.user.is_authenticated:
        return  redirect('login_user')
    user= User.objects.get(id= request.user.id)
    data = Signup.objects.get(user=user)
    error = False
    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        c = request.POST['contact']
        b = request.POST['branch']
        user.first_name = f
        user.last_name = l
        data.contact= c
        data.branch= b
        user.save()
        data.save()
        error= True

    d= {'data':data,'user':user, 'error' : error }
    return  render(request,'edit_profile.html',d)

def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method =='POST':
        b= request.POST['branch']
        s= request.POST['subject']
        n= request.FILES['notesfile']
        f= request.POST['filetype']
        d= request.POST['description']
        u= User.objects.filter(username= request.user.username).first()
        try:
            Notes.objects.create(user= u, uploadingdata= date.today(), branch= b, subject= s, 
                                notesfile=n, filetype= f, description= d,status='pending')
            error='no'
        
        except:
            error='yes'
    d= {'error':error}
    return render(request, 'upload_notes.html',d)


def view_mynotes(request):
    if not request.user.is_authenticated:
        return  redirect('login_user')
    user= User.objects.get(id= request.user.id)
    notes = Notes.objects.filter(user=user)
    d= {'notes':notes}
    return  render(request,'view_mynotes.html',d)

def delete_notes(request,id):
    if not request.user.is_authenticated:
        return redirect('login_user')

    notes= Notes.objects.get(id= id)
    notes.delete()
    return redirect('view_mynotes')

def delete_notes_admin(request,id):
    if not request.user.is_authenticated:
        return redirect('login_user')
    notes= Notes.objects.get(id= id)
    notes.delete()
    return redirect('all_notes')

def view_users(request):
    if not request.user.is_authenticated:
        return  redirect('login_admin')
    users = Signup.objects.all()
    d= {'users':users}
    return  render(request,'view_users.html',d)

def delete_user(request,id):
    if not request.user.is_authenticated:
        return redirect('login_user')
    user= User.objects.get(id =id)
    user.delete()
    return redirect('view_users')

def pending_notes(request):
    if not request.user.is_authenticated:
        return  redirect('login_admin')
    notes = Notes.objects.filter(status = 'pending' )
    d= {'notes':notes,'title':"VIEW PENDING NOTES"}
    return  render(request,'pending_notes.html',d)

def accept_notes(request):
    if not request.user.is_authenticated:
        return  redirect('login_admin')
    notes = Notes.objects.filter(status = 'Accept' )
    d= {'notes':notes,'title':"VIEW ACCEPT NOTES"}
    return  render(request,'pending_notes.html',d)

def reject_notes(request):
    if not request.user.is_authenticated:
        return  redirect('login_admin')
    notes = Notes.objects.filter(status = 'Reject' )
    d= {'notes':notes,'title':"VIEW REJECT NOTES"}
    return  render(request,'pending_notes.html',d)

def all_notes(request):
    if not request.user.is_authenticated:
        return  redirect('login_admin')
    notes = Notes.objects.all()
    d= {'notes':notes,'title':"VIEW ALL NOTES"}
    return  render(request,'pending_notes.html',d)

def assign_notes(request,id):
    if not request.user.is_authenticated:
        return redirect('login_user')

    notes= Notes.objects.get(id= id)
    error = ""
    if request.method == 'POST':
        s = request.POST['status']
        try:
            notes.status = s   
            notes.save() 
            error= "no"        
        except:
            error = "yes"
    d= {'notes':notes,'error':error}
    return render(request, 'assign_status.html',d)