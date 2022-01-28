from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('home/',home),
    path('contact',contact),
    path('about',about),
    path('register',register),
    path('check/',check),
    path('cancel/',cancel),
    path('MK Hotel And Resort/',hotel1),
    path('Hotel Royal King/',hotel2),
    path('Rosewood Resort/',hotel3),
    path('Hotel Haunted/',hotel4),
    path('check_date1/',check_date1),
    path('check_date2/',check_date2),
    path('check_date3/',check_date3),
    path('check_date/',check_date),
    # Payment
    path('payhome', payhome),
    path('success' , success)
    ]