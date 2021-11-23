from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name="home-page"),
    path('contact-page/', views.contactus, name="contact-page"),
]
