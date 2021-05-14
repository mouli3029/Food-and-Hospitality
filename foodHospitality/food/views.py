from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Food,Cart
from django.contrib.auth.models import User
from .forms import OrderForm
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
        'food_item' : food_item[0],
        'cid':cid,
    })

def FoodOrder(request,cid,fid):
    user_id = request.user.id
    user = get_object_or_404(User,pk=user_id)
    food = get_object_or_404(Food,pk=fid)
    category = get_object_or_404(Category,pk=cid)
    print(user)
    print(category)
    print(food)
    if request.method == "POST":
        filled_form = OrderForm(request.POST)
        if filled_form.is_valid():
           quantity = filled_form.cleaned_data['quantity']
           ordered_on = filled_form.cleaned_data['ordered_on']

           cart =  Cart(user=user,food=food,
                       quantity=quantity,ordered_on=ordered_on)
           cart.save()
           mess = "Thanks for ordering!Your order is successfull. Futher queries contact admin@gmail.com"
        else :
            mess = "Sorry something went wrong!Our team is working on it.Please try in few minutes"
        return render(request,'food/order_form.html',{
            'mess':mess,
            'filled_form':filled_form,
            'cid':cid,
            'fid':fid
    })

    else:
        cart = OrderForm()
        cart.fields['username'].initial = user.username
        cart.fields['email'].initial = user.email
        cart.fields['name'].initial = food.name
        cart.fields['category'].initial = category.cname

        return render(request,'food/order_form.html',{
            'form':cart,
             'cid':cid,
            'fid':fid
        })


        
