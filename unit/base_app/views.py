from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html',{'name':'John Doe'})

def register(request):
    return render(request, 'register.html', {'name':'Naveen  unkal'})

def men(request):
    return render(request, 'men.html')
def add(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])

    result = int(num1) + int(num2)
    multiplication = int(num1) * int(num2)
    print(multiplication)
    return render(request, 'add.html', {'result': result, 'multiplication': multiplication})