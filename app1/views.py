from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import user,category,menuitem,cart,cartitems
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def sigin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=User.objects.create_user(name,email,password)
        messages.success(request,'you have creted the account')
        return redirect('login')
    return render(request,'app1/sigin.html')

def login_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        user=authenticate(request,username=name,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  
        else:
            messages.error(request, 'Incorrect email or password. Please try again.')

            return redirect('login')  

    return render(request, 'app1/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"you have been looged out...!")
    return redirect('home')
    
def Category(request):
    Category=category.objects.all()
    return render(request, 'app1/order.html',{'Category':Category})

def menu(request,pk):
    category_instance = get_object_or_404(category, pk=pk)
    menu_items=menuitem.objects.filter(category=category_instance)
    return render(request, 'app1/menu.html', {'category_instance': category_instance, 'menu_items': menu_items})

def cart_use(request):
    data=json.loads(request.body)
    product_id=data['id']
    menu=menuitem.objects.get(id=product_id)
    if request.user.is_authenticated:
        Cart_instance,created = cart.objects.get_or_create(user=request.user, completed=False)
        Cartitems,created=cartitems.objects.get_or_create(cartitems=Cart_instance,menu=menu)
        Cartitems.quantity+=1
        Cartitems.save()
        print(Cartitems)
    else:
        return redirect('login') 
    return JsonResponse('it is working',safe=False)

def cartpage(request):
    Cart_instance,created = cart.objects.get_or_create(user=request.user, completed=False)
    Cartitems=cartitems.objects.filter(cartitems=Cart_instance)
    total_prize = 0
    for i in Cartitems:
        total_prize+= i.menu.price*i.quantity
    return render(request, 'app1/cart.html', {'Cartitems':Cartitems,'items':Cart_instance,'total_prize':total_prize})


def cartremove(request,pk):
    Cart=cartitems.objects.get(id=pk)
    Cart.delete()
    return redirect('cartpage')

def paymentsucces(request,pk):
    Cart=cart.objects.get(id=pk)
    cart.completed(True)
    messages.success(request,'payment made successfully')
    return redirect('home')