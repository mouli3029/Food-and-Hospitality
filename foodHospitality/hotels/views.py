from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Hotel
# Create your views here.


def AllHotels(request):
    hotels = Hotel.objects.all()
    return render(request,'hotels/viewhotels.html',{
        'hotels' : hotels
    })

def FetchHotel(request,id):
    hotel = get_object_or_404(Hotel,pk=id)
    return render(request,'hotels/hotel.html',{
        'hotel' : hotel
    })
  


