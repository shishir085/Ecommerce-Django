from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>You are in home page </h1>")
