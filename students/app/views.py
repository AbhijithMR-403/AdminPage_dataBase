from django.shortcuts import render,redirect,HttpResponse
from app.models import student
# Create your views here.
def user_log_in_page(request):
    if request.method == 'POST':
        
        return redirect('user_log_in_page')
    return render(request,'user_partition/login.html')

def user_sign_up_page(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if not name:
            print('Name is not right')
            return redirect('user_sign_up_page',{'name1':name})
        myUser=student(name=name,email=email,password=password)
        # myUser.save()
        return redirect('user_sign_up_page')
    return render(request,'user_partition/signup.html')

def user_home_page(request):
    return render(request,'user_partition/home.html')

def user_feature_page(request):
    return render(request,'user_partition/feature.html')

def user_price_page(request):
    return render(request,'user_partition/price.html')