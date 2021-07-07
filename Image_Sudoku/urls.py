from os import name
from django.urls import path
from . import views

urlpatterns = {
    path('',views.index, name='Home'),
    #path('',views.process, name='Process'),
}