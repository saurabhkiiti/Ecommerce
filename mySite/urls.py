from django.urls import path
from . import views

app_name = "mySite"
urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkOut/", views.checkOut, name="checkOut"),
    path("update_item/", views.updateItem, name="update_item"),
    path("process_order", views.processOrder, name="process_order"),
    path("register/", views.register, name="register"),
    path("login/", views.loginProcess, name="login"),
]