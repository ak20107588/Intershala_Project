from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.login),
   path('dashboard',views.dashboard),
   path('doctor',views.doctor),
   path('messages',views.messages1),
   path('signup',views.signup_detail),
   path('login_detail',views.login_detail),
   path('logout',views.logout),
   
]
