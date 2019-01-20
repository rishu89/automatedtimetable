from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url('^login',"autott.views.autott_login", name='login_url'),
    url(r'^signup', "autott.views.autott_signup", name='signup_url'),
]