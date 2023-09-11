from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('About/',about,name="about"),
    path('doctor/',doctor,name="doctor"),
    path('contact/',contact,name="contact"),
    path('shop/',shop,name="shop"),
    path('login/',userlogin,name="userlogin"),
]
