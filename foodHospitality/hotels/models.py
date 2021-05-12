from django.db import models  
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/hotels')
    rating = models.DecimalField(max_digits = 5,decimal_places = 1)
    price = models.DecimalField(max_digits = 10,decimal_places = 2,default=0)

    def __str__(self):
        return self.name   
# class Cart(models.Model):
#     product = models.ForeignKey(Prod)