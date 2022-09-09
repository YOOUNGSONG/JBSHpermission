from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
from .models import Classroom


# Create your views here.
def start(request):
    context = {'start': "start"}
    return render(request, 'pybo/first.html', context)


def main(request):
    context={'main': 'main'}
    return render(request, 'pybo/main.html', context)


def create(request):
    classroomList = Classroom.objects.order_by('-name')
    context={'time': timezone.now(), 'classrooms': classroomList}
    return render(request, 'pybo/create.html', context)


def join(request):
    context={}
    return render(request, 'pybo/join.html', context)


def user(request):
    context={}
    return render(request, 'pybo/user.jsp', context)