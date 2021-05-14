from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/food/')
    rating = models.DecimalField(max_digits = 5,decimal_places = 1)
    price = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Category(models.Model):
    cname  = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/category/')

    def __str__(self):
        return self.cname

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food = models.ForeignKey('Food',on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    ordered_on = models.DateField(default=date.today()) 
