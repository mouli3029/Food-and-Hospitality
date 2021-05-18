from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Hotel,Booking
from .forms import BookingForm
from django.contrib.auth.models import User
# Create your views here.


def AllHotels(request):
    query = request.GET.get('search')
    print(query)
    if(query):
        hotels = Hotel.objects.filter(name__contains=query)
        print(hotels)
        return render(request,'hotels/viewhotels.html',{
        'hotels' : hotels
    })

    hotels = Hotel.objects.all()
    return render(request,'hotels/viewhotels.html',{
        'hotels' : hotels
    })

def FetchHotel(request,id):
    hotel = get_object_or_404(Hotel,pk=id)
    return render(request,'hotels/hotel.html',{
        'hotel' : hotel
    })

def BookRoom(request,id):
    user_id = request.user.id
    user = get_object_or_404(User,pk=user_id)
    print(user)
    hotel = get_object_or_404(Hotel,pk=id)
    print(hotel)

    if request.method == 'POST':
        filled_form = BookingForm(request.POST)
        print(filled_form)
        if filled_form.is_valid():
            
            quantity = filled_form.cleaned_data['quantity']
            booked_from = filled_form.cleaned_data['booked_from']
            booked_to = filled_form.cleaned_data['booked_to']

            book_detail = Booking(user=user,hotel=hotel,quantity=quantity,booked_from=booked_from,booked_to=booked_to)
            book_detail.save()

            mess = {
                "title": "Thanks for booking.Your booking was successfull !",
                "ordername" : hotel.name,
                "booked_from":booked_from,
                "booked_to":booked_to
            }
        else:
            book_detail_id = None
            mess = {
                "title": "Sorry, for the inconvinence caused! Please try again",
                "ordername" : "",
                "booked_from":"",
                "booked_to":""
            }
        
        return render(request,'hotels/book_form.html',{
            "mess":mess,
            'filled_form':filled_form,
            'id':id,
        })
    else:
        form = BookingForm()
        form.fields['email'].initial = user.email
        form.fields['username'].initial = user.username
        form.fields['name'].initial = hotel.name + " " + "Hotel"
        return render(request,'hotels/book_form.html',{
            'form':form,
            'id':id,
            
        })
    return HttpResponse('<p>Booking Room</p>')

def YourBookings(request):
    user_id = request.user.id
    user = get_object_or_404(User,pk=user_id)
    bookings = Booking.objects.filter(user=user).values(
        'quantity',
        'booked_from',
        'booked_to',
        'hotel__name', # Similar to booking.hotel.value
        'hotel__price',
        'hotel__image',
        'id',
    )
    return render(request,'hotels/allbookings.html',{
        'bookings' : bookings
    })

def UpdateBooking(request,id):
    booking_details = get_object_or_404(Booking,pk=id)
    hotel_id = booking_details.hotel.id
    user_id = booking_details.user.id

    # Getting user and hotel based on booking
    hotel = get_object_or_404(Hotel,pk=hotel_id)
    user  = get_object_or_404(User,pk=user_id)

    
    # Post Method
    if request.method == "POST":
        filled_form = BookingForm(request.POST)
        print(filled_form)
        if filled_form.is_valid():
            
            quantity = filled_form.cleaned_data['quantity']
            booked_from = filled_form.cleaned_data['booked_from']
            booked_to = filled_form.cleaned_data['booked_to']

            book_detail = Booking(id=id,user=user,hotel=hotel,quantity=quantity,booked_from=booked_from,booked_to=booked_to)
            book_detail.save()

            mess = {
                "title" : "Updated Successfully!Please check in your bookings",
                "ordername" : hotel.name
            }
        else :
            mess = {
                "title" : "Something went wrong.We are working on it. Please try after few minutes !" ,
                "ordername": ""
                }
        return render(request,'hotels/booking_update.html',{
         'id' :id,
         "mess":mess
    })
    
    else :
        form = BookingForm()
        form.fields['email'].initial = user.email
        form.fields['username'].initial = user.username
        form.fields['name'].initial = hotel.name 
        form.fields['quantity'].initial = booking_details.quantity
        form.fields['booked_to'].initial = booking_details.booked_to

    print(booking_details)
    return render(request,'hotels/booking_update.html',{
        'form' : form,
        "id":id
    })
    

def BookStatus(request,id):
    return HttpResponse('<p> Booking Status </p>')




