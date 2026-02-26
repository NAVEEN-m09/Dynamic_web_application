from . import views
from django.urls import path

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="accounts_login"),
    path("logout/", views.logout_view, name="accounts_logout"),
]
