from django.urls import path,include
from .views import AllHotels,FetchHotel,BookRoom,YourBookings,UpdateBooking,DeleteBooking

urlpatterns = [
    path('all',AllHotels,name="hotels"),
    path('hotel/<int:id>/',FetchHotel,name="fetchhotel"),
    path('hotel/<int:id>/book',BookRoom,name="book"),
    path('allbookings',YourBookings,name="your"),
    path('allbookings/<int:id>/update',UpdateBooking,name="updateitem"),
    path('allbookings/<int:id>/delete',DeleteBooking,name="deleteitem"),
]