from django.shortcuts import render

# Create your views here.
def store(request):
    context={ }
    return render(request,'mySite/store.html',context)
def cart(request):
    context={ }
    return render(request,'mySite/cart.html',context)

def checkOut(request):
    context={ }
    return render(request,'mySite/checkOut.html',context)