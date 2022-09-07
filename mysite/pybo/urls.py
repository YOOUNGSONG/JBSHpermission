from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.start, name='start'),
    path('main/', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('join/', views.join, name='join'),
]
