from django.shortcuts import render,get_object_or_404,redirect
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
    food = []
    category = get_object_or_404(Category,pk=cid)
    
    query = request.GET.get('search')
    if(query):
        food = Food.objects.filter(name__contains=query,category=category)
        print(query)
        print(food)
        return render(request,'food/food.html',{
        'food' : food
    })

    category = get_object_or_404(Category,pk=cid)
    food = Food.objects.filter(category=category)
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
           address = filled_form.cleaned_data['address']
           cart =  Cart(user=user,food=food,address=address,
                       quantity=quantity,ordered_on=ordered_on)
           cart.save()
           mess = {
               "title" : "Thanks for ordering!Your order is successfull. Futher queries contact tasterideadmi6@gmail.com",
               "ordered_on":ordered_on,
               "ordername" : food.name,
           }
        else :
            mess = {
               "title" : "Sorry something went wrong!Our team is working on it.Please try in few minutes",
               "ordered_on":"",
               "ordername" : "",
              }
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


def AllOrders(request):
    user_id = request.user.id
    user = get_object_or_404(User,pk=user_id)

    # Function to calculate the total_price : 
    def calc_totalPrice(orders):
        total_price = 0
        for i in range(len(orders)):
            total_price  = total_price + orders[i]['quantity'] * orders[i]['food__price']
        return total_price

    orders = Cart.objects.filter(user=user).values(
        'quantity',
        'ordered_on',
        'food__name', 
        'food__price',
        'food__category__cname',
        'food__image',
        'address',
        'id'
    )
    return render(request,'food/cart.html',{
        'orders':orders,
        'total_price':calc_totalPrice(orders)
    })


def UpdateOrder(request,id):
    order_details = get_object_or_404(Cart,pk=id)
    food_id = order_details.food.id
    user_id = order_details.user.id

    # Getting user and hotel based on booking
    food = get_object_or_404(Food,pk=food_id)
    user  = get_object_or_404(User,pk=user_id)

    
    # Post Method
    if request.method == "POST":
        filled_form = OrderForm(request.POST)
        if filled_form.is_valid():
            
           quantity = filled_form.cleaned_data['quantity']
           ordered_on = filled_form.cleaned_data['ordered_on']
           address = filled_form.cleaned_data['address']
           cart =  Cart(id=id,user=user,food=food,address=address,
                       quantity=quantity,ordered_on=ordered_on)
           cart.save()
           mess = {
               "title" : "Your has been updated successfully.Futher queries contact tasterideadmi6@gmail.com",
               "ordered_on":ordered_on,
               "ordername" : food.name,
           }
        else :
            mess = {
                "title" : "Something went wrong.We are working on it. Please try after few minutes !" ,
                "ordername": ""
                }
        return render(request,'food/order_update.html',{
         'id' :id,
         "mess":mess
    })
    
    else :
        form = OrderForm()
        form.fields['email'].initial = user.email
        form.fields['username'].initial = user.username
        form.fields['name'].initial = food.name 
        form.fields['quantity'].initial = order_details.quantity
        form.fields['ordered_on'].initial = order_details.ordered_on
        form.fields['address'].initial = order_details.address,
        form.fields['category'].initial = food.category.cname

    return render(request,'food/order_update.html',{
        'form' : form,
        "id":id
    })

def DeleteOrder(request,id):
    status = Cart.objects.filter(pk=id).delete()
    return redirect('cart')
    

