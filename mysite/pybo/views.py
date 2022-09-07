from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def start(request):
    #return HttpResponse("Hello")
    context = {'start': "start"}
    return render(request, 'pybo/first.html', context)


def main(request):
    context={'main': 'main'}
    return render(request, 'pybo/main.html', context)


def create(request):
    context={}
    return render(request, 'pybo/create.html', context)


def join(request):
    context={}
    return render(request, 'pybo/join.html', context)