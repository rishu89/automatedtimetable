from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login',"autott.views.user_login", name='login_url'),
    url(r'^signup', "autott.views.user_signup", name='signup_url'),
]