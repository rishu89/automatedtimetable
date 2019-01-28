from django.urls import include, path
from django.contrib import admin
from . import views 


"""urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('signup/',views.user_signup, name='signup'),
]"""

urlpatterns = [
    path('trial/',views.home),
]