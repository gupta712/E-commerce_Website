from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .forms import CustomerRegistrationForm
from django.contrib import messages

class Product_view(View):
    def get(self, request):
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        top_wear = Product.objects.filter(category='TW')
        bottom_wear = Product.objects.filter(category='BW')
        return render(request, 'app/home.html', {'mobile': mobile, 'laptop': laptop, 'top_wear': top_wear, 'bottom_wear': bottom_wear})


class product_detail_view(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


class mobile_View(View):
    def get(self, request, data=None):
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
        return render(request, 'app/mobile.html', {'product_mobile': product_mobile})


class laptop_View(View):
    def get(self, request, data=None):
        if data == None:
            product_laptop = Product.objects.filter(category='L')
        elif data == 'Hp' or data == 'Dell':
            product_laptop = Product.objects.filter(
                category='L').filter(brand=data)
        return render(request, 'app/laptop.html', {'product_laptop': product_laptop})


class top_wear_View(View):
    def get(self, request, data=None):
        if data == None:
            product_topwear = Product.objects.filter(category='TW')
        elif data == 'Jockey' or data == 'Puma':
            product_topwear = Product.objects.filter(
                category='TW').filter(brand=data)
        return render(request, 'app/topwear.html', {'product_topwear': product_topwear})


class bottom_wear_View(View):
    def get(self, request, data=None):
        if data == None:
            product_bottomwear = Product.objects.filter(category='BW')
        elif data == 'Regular' or data == 'Roadster':
            product_bottomwear = Product.objects.filter(
                category='BW').filter(brand=data)
        return render(request, 'app/bottomwear.html', {'product_bottomwear': product_bottomwear})


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


class Customer_Profile_View(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        contact_number = request.POST.get('contact_number')
        image = request.FILES.get('image')
        if Customer_Profile.objects.filter(user=user):
            messages.success(request, 'profile already exists!')
            return render(request, 'app/profile.html')
        else:
            profile = Customer_Profile.objects.create(
            user=user, name=name, address=address, city=city, state=state, zip_code=zip_code, contact_number=contact_number, image=image)
            profile.save()
            messages.success(request, 'profile added successful!')
            return render(request, 'app/profile.html')
            
def view_profile(self,request):
    user = self.request.user
    profile = Customer_Profile.objects.get(user=user)
    return render(request, 'app/view_profile.html')
    
    
    

    

    
        
        
        
     


def profile(request):
    return render(request, 'app/profile.html')


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')


def checkout(request):
    return render(request, 'app/checkout.html')
