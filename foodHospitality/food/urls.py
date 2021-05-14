from django.urls import path
from .views import Menu,FoodView,FoodItem,FoodOrder

urlpatterns = [
    path('menu/',Menu,name='menu'),
    path('menu/<int:cid>/',FoodView,name='food'),
    path('menu/<int:cid>/<int:fid>',FoodItem,name="fooditem"),
    path('menu/<int:cid>/<int:fid>/order',FoodOrder,name="foodorder"),
]