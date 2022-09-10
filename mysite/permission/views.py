from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
from .models import Classroom, User


num = 0
name = ""


# Create your views here.
def start(request):
    userList = User.objects.order_by('-num')
    context = {'start': "start", 'users': userList}
    return render(request, 'permission/first.html', context)


def create(request):
    classroomList = Classroom.objects.order_by('-name')
    context={'time': timezone.now(), 'classrooms': classroomList, 'num': num, 'name': name}
    return render(request, 'permission/create.html', context)


def join(request):
    context={}
    return render(request, 'permission/join.html', context)


def main(request):
    global num, name
    num = int(request.POST.get('num'))
    name = str(request.POST.get('name'))

    valid = User.objects.get(num__exact=num)

    if num == valid.num and name == valid.name:
        context = {'num': num, 'name': name}
        return render(request, 'permission/main.html', context)
    else:
        return redirect('permission:start')


