from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginProcess(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "mySite/store.html")
        else:
            messages.info(request, "Username or password is incorrect")
    else:
        return render(request, "mySite/login.html")


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = Customer.objects.get_or_create(user=request.user)
            return render(request, "mySite/store.html")

    context = {"form": form}
    return render(request, "mySite/register.html", context)


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "mySite/store.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"cart_total": 0, "cart_items": 0}
    context = {"items": items, "order": order}
    return render(request, "mySite/cart.html", context)


def checkOut(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"cart_total": 0, "cart_items": 0}
    context = {"items": items, "order": order}
    return render(request, "mySite/checkOut.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]

    print("action: ", action)
    print("productId: ", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem, created = orderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderitem.quantity = orderitem.quantity + 1
    elif action == "remove":
        orderitem.quantity = orderitem.quantity - 1

    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse("Item added", safe=False)


def processOrder(request):
    print(request.body)
    return JsonResponse("COmplete", safe=False)
