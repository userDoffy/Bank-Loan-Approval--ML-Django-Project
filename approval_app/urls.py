from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('checkapproval',views.checkapproval,name='checkapproval'),
    path('logout',views.loggout,name='logout'),
]