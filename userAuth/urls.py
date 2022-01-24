from django.urls import path
from .views import *

app_name = 'otentik'
urlpatterns = [
    path('login',signin,name='login'),
    path('register',Register.as_view(),name='register'),
    path('signout/', signout, name='logout'),
    path('getregencies',getRegencies,name='get_regencies')
]
