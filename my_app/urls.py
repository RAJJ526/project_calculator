from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
   
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.AboutView.as_view(), name='post'),
]
