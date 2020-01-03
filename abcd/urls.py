from django.contrib import admin
from django.urls import path
from abcd import views
from abcd.views import home,title

urlpatterns = [
    path('', views.home,name='home'),
    path('title',views.title,name = 'title'),
     path('error',views.title,name = 'error'),

]
