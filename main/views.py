from imaplib import _Authenticator
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from .models import *

def group_required(*group_names):
    def in_group(u):
        return (u.is_superuser or bool(u.groups.filter(name__in=group_names)))
    return user_passes_test(in_group)

# Create your views here.
def index(request):
    category = Category.objects.all()
    context = {"category":category}
    return render (request, 'index.html',context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username).first()
        # vendor = Vendorregistration.objects.get(user = user_obj)
        

        if user_obj is None:
            messages.error(request, 'User not found')
            return redirect('/login')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('/')
        else:
            messages.error(request, 'Wrong password or email')
            return redirect('/login')
    
    
    return render (request, 'login.html')

def vendorsignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username).first()
        vendor = Vendorregistration.objects.get(user = user_obj)
        

        if user_obj is None:
            messages.error(request, 'User not found')
            return redirect('/login')
        
        user = authenticate(username=username,password=password)

        if user is not None:
            if vendor is not None:
                if vendor.usertype == "vendor":
                    login(request, user)
                    messages.success(request, 'Login successfully')
                    return redirect('/dashboard')
        else:
            messages.error(request, 'Wrong password or email')
            return redirect('/login')



    return render (request, 'vendorlogin.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if len(password) < 6:
                messages.error(request,'Password is too short.')
            if User.objects.filter(username=username).first():
                messages.error(request,'Username is taken.')
                return redirect('/')
            if User.objects.filter(email = email).first():
                messages.error(request,'Email id is taken.')
                return redirect('/')
            
            user_obj = User(username=username,email=email)
            user_obj.set_password(password)
            if user_obj:
                user_obj.save()
                messages.success(request,'Registration successfully.')

        except Exception as e:
            print(e)

    return render (request, 'register.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('/')

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        fn = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')

        try:
            message = fn + email + msg
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
            messages.success(request, 'successfully send')
            return redirect('/')
        except Exception as e:
            print(e)
    return render(request,'contact_us.html')

def singlecategory(request,category):
    # category_obj = Category.objects.get(category=category)
    category_obj = Categorydetails.objects.filter(category=category)
    # print(category_obj)
    print(category_obj)
    # category_obj = Categorydetails.objects.filter() 
    context = {"category":category_obj}
    return render(request,'singlecategory.html',context)
@login_required(login_url='login')
def categorydetails(request,title):
    categorydetails = Categorydetails.objects.filter(title=title)
    context = {"categorydetails":categorydetails}
    return render(request,'categorydetails.html',context)



def bookservice(request,title):
    if request.method == 'POST':
        fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        date = request.POST.get('date')
        time = request.POST.get('time')
        categorydetails = Categorydetails.objects.get(title=title)
        booking = Booking(
            category = categorydetails,
            fullname = fullname,
            email = email,
            contactno = contactno,
            days = date,
            timing = time
       )
        if booking:
            booking.save()
            messages.success(request, 'Booking successfully.')
        
       

    return render(request,'booking.html')


def about(request):
     return render(request,'about.html')

@group_required('vendor')
def dashboard(request):
     vendor = Vendorregistration.objects.all()
     context = {"vendor":vendor}
     return render(request,'dashboard.html',context)

def addservice(request):
     if request.method == "POST":
         category = request.POST.get('category')
         title = request.POST.get('title')
         desc = request.POST.get('desc')
         min_price = request.POST.get('min_price')
         max_price = request.POST.get('max_price')
         logo_image = request.FILES['logoimage']
         services = request.POST.get('services')
         days = request.POST.get('days')
         time = request.POST.get('time')
         location = request.POST.get('location')
         email = request.POST.get('email')
         image1 = request.FILES['image1']
         image2 = request.FILES['image2']
         image3 = request.FILES['image3']
         image4 = request.FILES['image4']
         vendor = Vendorregistration.objects.get(user=request.user)

         category_obj = Categorydetails(
            vendor = vendor,
            category = category,
            title = title,
            desc = desc,
            min_price = min_price,
            max_price = max_price,
            logo_image = logo_image,
            services = services,
            days = days,
            timing = time,
            location = location,
            email = email,
            image1 = image1,
            image2 = image2,
            image3 = image3,
            image4 = image4
         )
         if category_obj:
            category_obj.save()
            messages.success(request, 'service register successfully.')

         
         
     return render(request,'addservice.html')

def allservice(request):
     vendor_obj = Vendorregistration.objects.get(user=request.user)
     category_obj = Categorydetails.objects.filter(vendor=vendor_obj)
     context = {"service":category_obj}
     return render(request,'allservice.html',context)

def bookinglist(request):
     vendor_obj = Vendorregistration.objects.get(user=request.user)
     category_obj = Categorydetails.objects.all()
     booking_obj = Booking.objects.all()
     context = {"booking":booking_obj}
     return render(request,'bookinglist.html',context)

def vendorregi(request):
    if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            usertype = "vendor"

            try:
                if len(password) < 6:
                    messages.error(request,'Password is too short.')
                if User.objects.filter(username=username).first():
                    messages.error(request,'Username is taken.')
                    return redirect('/')
                if User.objects.filter(email = email).first():
                    messages.error(request,'Email id is taken.')
                    return redirect('/')
                
                user_obj = User(username=username,email=email)
                user_obj.set_password(password)
                user_obj.save()
                vendor_obj = Vendorregistration.objects.create(user=user_obj,usertype=usertype)
                # if vendor_obj:
                vendor_obj.save()
                group = Group.objects.get(name=usertype)
                user_obj.groups.add(group)
                messages.success(request,'Registration successfully.')

            except Exception as e:
                print(e)

    return render(request,'vendor_registration.html')


# def chatbot(request):
#     if request.method == 'POST':
#         question = request.POST.get('question')
#         try:
#             chat = Chat.objects.get(question=question)
#             answer = chat.answer
#         except Chat.DoesNotExist:
#             answer = "Sorry, I don't understand your question."
#         return JsonResponse({'answer': answer})
#     else:
#         return render(request, 'chatbot.html')