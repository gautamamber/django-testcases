from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration/', views.UserRegistrationView.as_view(), name = 'register')
]