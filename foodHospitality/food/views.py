from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
# Create your views here.

def Menu(request):
    menu = Category.objects.all()
    return render(request,'food/menu.html',{
        'menu' : menu
    })

def Food(request,cid):
    return HttpResponse('<p>Food</p>')


def FoodItem(request,cid,fid):
    return HttpResponse('<p>Food Item</p>')
