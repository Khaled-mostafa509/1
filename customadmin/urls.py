from django.contrib import admin
from django.urls import path, include
from .views import *

app_name ='customadmin'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', admin_login , name = "admin_login"),
    path('dashboard/', dashboard , name = "dashboard"),

]