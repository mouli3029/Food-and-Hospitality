from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel
# Create your views here.


def AllHotels(request):
    hotels = Hotel.objects.all()
    return render(request,'hotels/viewhotels.html',{
        'hotels' : hotels
    })

def FetchHotel(request,id):
    return HttpResponse('<p> Fetch single hotel {{id}} </p>')
  


