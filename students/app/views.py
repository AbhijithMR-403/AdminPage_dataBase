from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_log_in_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(username=name,password=password)
        if user:
            if user.is_superuser is False:
                login(request,user)
                return redirect('home')
        else:
            messages.warning(request,'Not a valid username or password')
            return redirect('user_log_in_page')

        
    return render(request,'user_partition/login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_sign_up_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # ^ Checking for validation of those things type in form
        if not name and not email and not password:
            messages.warning(request,'Type something to register')
            return redirect('user_sign_up_page')

        if not name:
            messages.warning(request,'Type your name')
            return redirect('user_sign_up_page')
        if not email:
            messages.warning(request,'Type your email')
            return redirect('user_sign_up_page')
        if not password:
            messages.warning(request,'Type your password')
            return redirect('user_sign_up_page')
        
        
        # *Storing to database 
        try:
            if User.objects.get(username=name):
                messages.warning(request,'This name already exist')
                return redirect('/reg')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,'This email is already taken')
                return redirect('/reg')
        except:
            pass
        
        myUser=User.objects.create_user(name,email,password)
        myUser.save()
        return redirect('/')
    return render(request,'user_partition/signup.html')


def user_home_page(request):
    return render(request,'user_partition/home.html')

def user_feature_page(request):
    return render(request,'user_partition/feature.html')

def user_price_page(request):
    return render(request,'user_partition/price.html')
    
def user_log_out(request):
    logout(request)
    return redirect('/')

def admin_login_page(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(username=name,password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('admin_home')
        else:
            return redirect('')
    return render(request,'admin_paritition/login.html')

def admin_sign_up_page(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # ^ Checking for validation of those things type in form
        if not name and not email and not password:
            messages.warning(request,'Type something to register')
            return redirect('user_sign_up_page')

        if not name:
            messages.warning(request,'Type your name')
            return redirect('admin_sign_up_page')
        if not email:
            messages.warning(request,'Type your email')
            return redirect('admin_sign_up_page')
        if not password:
            messages.warning(request,'Type your password')
            return redirect('admin_sign_up_page')
        
        # *Storing to database 
        try:
            if User.objects.get(username=name):
                messages.warning(request,'This name already exist')
                return redirect('admin_sign_up_page')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,'This email is already taken')
                return redirect('admin_sign_up_page')
        except:
            pass
        
        myUser=User.objects.create_user(name,email,password)
        myUser.save()
        return redirect('/')
    return render(request,'admin_paritition/signup.html')

def admin_home_page(request):
    person=User.objects.all()
    print(person)
    pp={'p':person,'k':'ajith is here'}
    return render(request,'admin_paritition/adminpage.html',pp)