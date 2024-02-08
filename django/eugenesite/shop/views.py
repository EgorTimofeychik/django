from django.shortcuts import render
from django.http import HttpResponse


def my_blog(request):
    return HttpResponse("Hello from my shop!")


def my_blog1(request):
    return HttpResponse("Hello from article 1!")


def my_blog2(request):
    return HttpResponse("Hello from article 2!")
