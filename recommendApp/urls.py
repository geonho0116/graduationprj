from django.urls import path
from .views import *


app_name = 'recommendApp'

urlpatterns = [
    path('',index,name='index'),
    path('result/',new, name='result'),

]