from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Food
# Create your views here.

def Menu(request):
    menu = Category.objects.all()
    return render(request,'food/menu.html',{
        'menu' : menu
    })

def FoodView(request,cid):
    print(cid)
    category = get_object_or_404(Category,pk=cid)
    food = Food.objects.filter(category=category)
    print(food)

    return render(request,'food/food.html',{
        'food' : food
    })


def FoodItem(request,cid,fid):

    category = get_object_or_404(Category,pk=cid)
    food = Food.objects.filter(category=category)
    food_item = food.filter(id=fid)
    return render(request,'food/food_item.html',{
        'food_item' : food_item[0]
    })
