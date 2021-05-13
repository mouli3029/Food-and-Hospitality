from django.db import models  
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/hotels')
    rating = models.DecimalField(max_digits = 5,decimal_places = 1)
    price = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)

    def __str__(self):
        return self.name   

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    booked_from = models.DateField(default=date.today())
    booked_to = models.DateField()