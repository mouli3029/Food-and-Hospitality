from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def AllHotels(request):
    return HttpResponse('<p> All hotels</p>')

def FetchHotel(request,id):
    return HttpResponse('<p> Fetch single hotel {{id}} </p>')
  


