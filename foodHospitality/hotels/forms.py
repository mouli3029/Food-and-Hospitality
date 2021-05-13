from django import forms
from .models import Booking,Hotel

class BookingForm(forms.ModelForm):
    email = forms.EmailField()
    username =  forms.CharField()
    phone_no = forms.CharField(max_length=12)
    name = forms.CharField(max_length=50)
    class Meta:
        model = Booking
        fields = ['username','email','phone_no','name','quantity','booked_from','booked_to']



