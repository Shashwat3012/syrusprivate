# This file is for testing the Django Website for our ASAP Project.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Truck, Test
from .models import User, Truck


def login(request):
    # return render(request, 'login.html')
    # ls = Truck.objects.get(id=id)
    # return HttpResponse("<h1>%s</h1>" %ls.name)

    params = {'name': 'Shashwat', 'place': 'Mars'}
    return render(request, 'login.html', params)
    # return HttpResponse('''<h1>shashwat</h1>'''
    #                     '''<a href="https://stackoverflow.com/">Stack Overflow</a><br>'''
    #                     '''<a href="https://www.geeksforgeeks.org/">GFG</a><br>'''
    #                     '''<a href="https://www.youtube.com/">Youtube</a><br>'''
    #                     '''<a href="https://twitter.com/">Twitter</a><br>'''
    #                     '''<a href="https://linkedin.com/">LinkedIn</a><br>'''
    #                     '''<a href="/about">About</a><br>''')


def register(request):
    if request.method == "POST":
        signup_name = request.POST['fullname']
        signup_username = request.POST['username']
        signup_mobile = request.POST['mobile']
        signup_email = request.POST['email']
        signup_password = request.POST['password']

    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def carbonfootprint(request):
    return render(request, 'carbonfootprint.html')


def truck_list(request):
    trucks = Truck.objects.all()
    return render(request, 'truck_list.html', {'trucks': trucks})


def business(request):
    return render(request, 'business.html')


def truckowner(request):
    return render(request, 'truckowner.html')


def newshipping(request):
    return render(request, 'newshipping.html')

def requestshipping(request):
    return render(request, 'requestshipping.html')


def calculator(request):
    return render(request, 'carbonfootprint.html')

def save_user(request):
    if request.method == "POST":
        register_name = request.POST.get('fullname')
        register_username = request.POST.get('username')
        register_mobile = request.POST.get('mobile')
        register_email = request.POST.get('email')
        register_password = request.POST.get('password')
        register_role = request.POST.get('role')
        cursor = User(name=register_name, username=register_username, phone=register_mobile, email=register_email,
                      password=register_password, role=register_role)
        cursor.save()

    users = User.objects.all()
    return render(request, 'register.html', {'user': users})


def test_method(request):
    tests = Test.objects.all()
    return render(request, 'home.html', {'test': tests})


