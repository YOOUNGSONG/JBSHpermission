from django.urls import path
from . import views

app_name = 'permission'

urlpatterns = [
    path('', views.start, name='start'),
    path('main/', views.main, name='main'),
    path('main/create/', views.create, name='create'),
    path('main/join/', views.join, name='join'),
    path('usercheck/', views.user, name='usercheck'),
    path('user/create/<int:user_id>/', views.user, name='user_create')
]
