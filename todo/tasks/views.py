from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse('Hello World')


def task_list(request):
    return render(request, 'tasks/list.html')
