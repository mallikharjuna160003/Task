from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('index/',views.index,name="index"),
    path('profile/',views.profile,name="profile"),

]