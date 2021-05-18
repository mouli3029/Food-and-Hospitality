from django.urls import path,include
from .views import AllHotels,FetchHotel,BookRoom,BookStatus,YourBookings,UpdateBooking

urlpatterns = [
    path('all',AllHotels,name="hotels"),
    path('hotel/<int:id>/',FetchHotel,name="fetchhotel"),
    path('hotel/<int:id>/book',BookRoom,name="book"),
    path('hotel/<int:id>/book/status',BookStatus,name="bookstatus"),
    path('allbookings',YourBookings,name="your"),
    path('allbookings/<int:id>/update',UpdateBooking,name="updateitem"),
]