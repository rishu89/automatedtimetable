from django.conf.urls import include, url
from django.contrib import admin
from  . import views 


urlpatterns = [
    url('login/',views.user_login),
    url('signup/',views.users_signup),
]