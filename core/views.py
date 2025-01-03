from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome to social book</h1>')