from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
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
        if user := authenticate(username=name, password=password):
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
        if not email or '@' not in email:
            messages.warning(request,'Invalid email')
            return redirect('user_sign_up_page')
        if not password or len(password)<4:
            messages.warning(request,'Type more character\' for password')
            return redirect('user_sign_up_page')
        
        # *Storing to database 
        try:
            if User.objects.get(username=name):
                messages.warning(request,'This name already exist')
                return redirect('user_sign_up_page')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,'This email is already taken')
                return redirect('user_sign_up_page')
        except:
            pass
        
        myUser=User.objects.create_user(name,email,password)
        myUser.save()
        return redirect('/')
    return render(request,'user_partition/signup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_home_page(request):
    if request.user.is_authenticated:
        return render(request,'user_partition/home.html')
    return redirect('user_log_in_page')
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_feature_page(request):
    if request.user.is_authenticated is None:
        return render(request,'user_partition/feature.html')
    return redirect('user_log_in_page')
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_price_page(request):
    if request.user.is_authenticated is None:
        return render(request,'user_partition/price.html')
    return redirect('user_log_in_page')
    

    
def user_log_out(request):
    logout(request)
    return redirect('/')

def admin_log_out(request):
    logout(request)
    return redirect('admin_log_in_page')


# ^Admin partition side

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login_page(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_home')

    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(username=name,password=password)
        print(user,'\n\n\n\n')
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('admin_home')
        else:
            messages.warning(request,'Detail\'s are not correct')
            return redirect('admin_log_in_page')
    return render(request,'admin_paritition/login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_home_page(request):
    if request.user.is_authenticated and request.user.is_superuser:
        person=User.objects.all().exclude(is_superuser=True).order_by('id')
        
        pp={'p':person,'k':'ajith is here'}
        return render(request,'admin_paritition/adminpage.html',pp)
    return redirect('admin_log_in_page')

def delete_row(request,row_id):
    details = get_object_or_404(User, id=row_id)
    details.delete()
    messages.warning(request,'Data is deleted successfully')
    return redirect('admin_home')

def admin_edit(request,row_id):
    details = get_object_or_404(User, id=row_id)
    return render(request,'admin_paritition/edit.html',{'details':details})

def admin_edit_submit(request,row_id):
    # if request.method == 'POST':
        user = User.objects.get(id=row_id)
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        user.username=name
        user.email=email
        if password:
            user.password=password
        messages.success(request,'Data is edited successfully')
        user.save()
        return redirect('admin_home')
        
def admin_search(request):
    if request.method == 'POST':
        username = request.POST.get('search_admin', '')

        if username: 
            person = User.objects.filter(username__icontains=username)
            pp = {'p': person} 
            return render(request, 'admin_paritition/adminpage.html', pp) 

    return redirect("admin_home")

def create_user_admin(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # ^ Checking for validation of those things type in form
        if not name and not email and not password:
            messages.warning(request,'Type something to register')
            return redirect('create_user_admin')

        if not name:
            messages.warning(request,'Type your name')
            return redirect('create_user_admin')
        if not email or '@' not in email:
            messages.warning(request,'Invalid email')
            return redirect('create_user_admin')
        if not password or len(password)<4:
            messages.warning(request,'Type more character\' for password')
            return redirect('create_user_admin')
        
        # *Storing to database 
        try:
            if User.objects.get(username=name):
                messages.warning(request,'This name already exist')
                return redirect('create_user_admin')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,'This email is already taken')
                return redirect('create_user_admin')
        except:
            pass
        
        myUser=User.objects.create_user(name,email,password)
        myUser.save()
        return redirect('admin_home')




    return render(request,'admin_paritition/createuser.html')