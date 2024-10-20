from django.urls import path 
from .views import *

urlpatterns = [
    path('register' ,register,name='register'),
    path('' ,login_view,name='login'),
    path('dashboard' , dashboard , name="dashboard"),
    path('logout/',logout_view , name="logout"),
]