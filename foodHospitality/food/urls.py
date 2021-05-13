from django.urls import path
from .views import Menu,Food,FoodItem

urlpatterns = [
    path('menu/',Menu,name='menu'),
    path('menu/<int:cid>/',Food,name='food'),
    path('menu/<int:cid>/<int:fid>',FoodItem,name="fooditem")
]