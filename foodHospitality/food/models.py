from django.db import models

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
