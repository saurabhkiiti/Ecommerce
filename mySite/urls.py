from django.urls import path
from . import views

app_name='mySite'
urlpatterns = [
    path('',views.store,name='store'),
path('cart/',views.cart,name='cart'),
path('checkOut/',views.checkOut,name='checkOut')
]