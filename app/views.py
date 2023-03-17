from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

class Product_view(View):
    def get(self, request):
        totalitem = 0
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        top_wear = Product.objects.filter(category='TW')
        bottom_wear = Product.objects.filter(category='BW')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        return render(request, 'app/home.html', {'mobile': mobile, 'laptop': laptop, 'top_wear': top_wear, 'bottom_wear': bottom_wear,'totalitem':totalitem})

@method_decorator(login_required, name='dispatch')
class product_detail_view(View):
    # totalitem = 0
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        cart_item_already = False
        if request.user.is_authenticated:
            cart_item_already = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
            print(cart_item_already)
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))

            return render(request, 'app/productdetail.html', {'product': product,'cart_item_already':cart_item_already})

@method_decorator(login_required, name='dispatch')
class mobile_View(View):
    def get(self, request, data=None):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        if data == None:
            product_mobile = Product.objects.filter(category='M')
        elif data == 'Redmi' or data == 'Samsung':
            product_mobile = Product.objects.filter(
                category='M').filter(brand=data)
        elif data == 'below':
            product_mobile = Product.objects.filter(
                category='M').filter(discounted_price__lt=10000)
        elif data == 'above':
            product_mobile = Product.objects.filter(
                category='M').filter(discounted_price__gt=10000)
        return render(request, 'app/mobile.html', {'product_mobile': product_mobile,'totalitem':totalitem})

@method_decorator(login_required, name='dispatch')
class laptop_View(View):
    
    def get(self, request, data=None):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        if data == None:
            product_laptop = Product.objects.filter(category='L')
        elif data == 'Hp' or data == 'Dell':
            product_laptop = Product.objects.filter(
                category='L').filter(brand=data)
        return render(request, 'app/laptop.html', {'product_laptop': product_laptop,'totalitem':totalitem})

@method_decorator(login_required, name='dispatch')
class top_wear_View(View):
    def get(self, request, data=None):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        if data == None:
            product_topwear = Product.objects.filter(category='TW')
        elif data == 'Jockey' or data == 'Puma':
            product_topwear = Product.objects.filter(
                category='TW').filter(brand=data)
        return render(request, 'app/topwear.html', {'product_topwear': product_topwear,'totalitem':totalitem})

@method_decorator(login_required, name='dispatch')
class bottom_wear_View(View):
    def get(self, request, data=None):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        if data == None:
            product_bottomwear = Product.objects.filter(category='BW')
        elif data == 'Regular' or data == 'Roadster':
            product_bottomwear = Product.objects.filter(
                category='BW').filter(brand=data)
        return render(request, 'app/bottomwear.html', {'product_bottomwear': product_bottomwear,'totalitem':totalitem})


class CustomerRegistrationView(View):
    def get(self, request):


        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations !! Successfully Registered')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})
@login_required
def profile_view(request):
   
    if request.method=="POST":
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
   
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        contact_number = request.POST.get('contact_number')
        image = request.FILES.get('image')
        profile = Customer_Profile.objects.create(
        user=user, name=name, address=address, city=city, state=state, zip_code=zip_code, contact_number=contact_number, image=image)
        profile.save()
        messages.success(request, 'profile added successful!')
        return render(request, 'app/profile.html',{'active':'btn-primary','totalitem':totalitem})
    return render(request, 'app/profile.html',{'active':'btn-primary'})
@login_required      
def address(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    user = request.user
    address = Customer_Profile.objects.filter(user=user)
    return render(request, 'app/address.html',{'address':address,'active':'btn-primary','totalitem':totalitem})

    
@login_required 
def addtocart(request):  
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user = user,product=product).save()
    return redirect('/cart')
    
                
        
    
@login_required
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        totalitem = 0
   
        totalitem = len(Cart.objects.filter(user=request.user))
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
      
        if cart_product:
            for p in cart_product:
                
                temprary = (p.quantity*p.product.discounted_price)
                
                amount += temprary
                total_amount = amount+shipping_amount
                
            return render(request, 'app/addtocart.html',{'cart':cart,'total_amount':total_amount,'amount':amount,'totalitem':totalitem})
        else:
            return render(request, 'app/emptycart.html')
   
@login_required       
def plus_cart(request):
    
    if request.method == "GET":
        
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        
        for p in cart_product:
            temprary = (p.quantity*p.product.discounted_price)
            amount += temprary
            total_amount = amount+shipping_amount
            data = {
                'amount':amount,
                'total_amount':total_amount,
                'quantity':c.quantity
            }
        return JsonResponse(data)
@login_required   
def minus_cart(request):
    
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        
        for p in cart_product:
            temprary = (p.quantity*p.product.discounted_price)
            amount += temprary
            total_amount = amount+shipping_amount
            data = {
                'amount':amount,
                'total_amount':total_amount,
                'quantity':c.quantity
            }
        return JsonResponse(data)
@login_required    
def remove_cart(request):
    
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        
        for p in cart_product:
            temprary = (p.quantity*p.product.discounted_price)
            amount += temprary
            
        data = {
            'amount':amount,
            'total_amount':amount+shipping_amount
            
        }
        return JsonResponse(data)
               
        
@login_required
def buy_now(request):
    return render(request, 'app/buynow.html')



@login_required
def orders(request):
    order = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order':order})

# def change_password(request):
#  return render(request, 'app/changepassword.html')

@login_required
def checkout(request):
    user = request.user
    customer = Customer_Profile.objects.filter(user=user)
  
    cart_item = Cart.objects.filter(user=user)
    
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user==user]
   
    if cart_product:
        for p in cart_product:
            
            temprary = (p.quantity*p.product.discounted_price)
            amount += temprary
            total_amount = amount+shipping_amount

    return render(request, 'app/checkout.html',{'total_amount':total_amount,'customer':customer,'cart_item':cart_item})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer_Profile.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        print(c,"hello")
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()

    return redirect('orders')
