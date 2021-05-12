from django.urls import path,include
from .views import AllHotels,FetchHotel

urlpatterns = [
    path('all',AllHotels,name="hotels"),
    path('hotel/<int:id>/',FetchHotel,name="fetchhotel"),
]