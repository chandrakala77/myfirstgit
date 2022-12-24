from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse


# Create your views here.
def chandu(request):
    return HttpResponse('chandu')

def laddu(request):
    return HttpResponse('laddu')


