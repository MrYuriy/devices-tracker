from django.shortcuts import render
from django.http import HttpResponse

def not_sleep(request):
    return HttpResponse(status=200)
