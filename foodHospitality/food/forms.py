from django import forms
from .models import Cart

class OrderForm(forms.ModelForm):
    email = forms.EmailField()
    username =  forms.CharField()
    phone_no = forms.CharField(max_length=12)
    name = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    
    class Meta:
        model = Cart
        fields = ['username','email','phone_no','name','category','quantity','orderedOn']



