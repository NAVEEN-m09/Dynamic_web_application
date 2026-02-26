from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Appointment, unit


# Create your views here.
def index(request):
    some_unit1 = unit()
    some_unit1.name = "hey its a new version"
    some_unit1.price = 100
    some_unit1.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    some_unit1.img = "assets/img/services/services1.jpg"

    #unit1
    some_unit2 = unit()
    some_unit2.name = "hey its a new version"
    some_unit2.price = 200
    some_unit2.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    some_unit2.img = "assets/img/services/services2.jpg"

    #unit3
    some_unit3=unit()
    some_unit3.name = "hey its a new version"
    some_unit3.price = 300
    some_unit3.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    some_unit3.img = "assets/img/services/services3.jpg"

    
      
    return render(request, "index.html", {"some_unit1": some_unit1, "some_unit2": some_unit2, "some_unit3": some_unit3})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def elements(request):
    return render(request, 'elements.html')

def contact(request):
    return render(request, 'contact.html')


def appointment(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        appointment_date = request.POST.get("appointment_date", "").strip()
        appointment_time = request.POST.get("appointment_time", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not phone or not appointment_date or not appointment_time:
            return render(
                request,
                "appointment.html",
                {
                    "error": "Name, phone, date, and time are required.",
                    "form_data": request.POST,
                },
            )

        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            message=message,
        )
        return redirect(f"{reverse('appointment')}?success=1")

    return render(request, "appointment.html", {"success": request.GET.get("success") == "1"})

