from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def register(request):
    form_data = {}

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        terms = request.POST.get("terms")

        form_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
        }

        if not all([first_name, last_name, email, phone, password, confirm_password]):
            messages.error(request, "Please fill all required fields.")
        elif password != confirm_password:
            messages.error(request, "Password and confirm password do not match.")
        elif not terms:
            messages.error(request, "Please accept terms and conditions.")
        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, "This email is already registered.")
        else:
            # Using email as username keeps the existing form simple.
            User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("register")

    return render(request, "accounts/register.html", {"form_data": form_data})


def login_view(request):
    form_data = {}

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        form_data = {"email": email}

        if not email or not password:
            messages.error(request, "Please enter email and password.")
        else:
            user = authenticate(request, username=email, password=password)
            if user is None:
                messages.error(request, "Invalid email or password.")
            else:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect("index")

    return render(request, "accounts/login.html", {"form_data": form_data})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("index")
