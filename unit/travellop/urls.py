from . import views 
from django.urls import path 

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),

    path('about/', views.about, name='about'),
    path('about.html', views.about, name='about_html'),

    path('services/', views.services, name='services'),
    path('services.html', views.services, name='services_html'),

    path('blog/', views.blog, name='blog'),
    path('blog.html', views.blog, name='blog_html'),

    path('blog_details/', views.blog_details, name='blog_details'),
    path('blog_details.html', views.blog_details, name='blog_details_html'),

    path('elements/', views.elements, name='elements'),
    path('elements.html', views.elements, name='elements_html'),

    path('contact/', views.contact, name='contact'),
    path('contact.html', views.contact, name='contact_html'),

    path('appointment/', views.appointment, name='appointment'),
    path('appointment.html', views.appointment, name='appointment_html'),
]
