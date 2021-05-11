from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    phone_no = forms.CharField(max_length=12)

    class Meta : 
        model = User
        fields = ['username','email','phone_no','password1','password2']