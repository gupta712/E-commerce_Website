from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer_Profile,Cart,OrderPlaced,Product
admin.site.register(Cart)
admin.site.register(Customer_Profile)
admin.site.register(OrderPlaced)
admin.site.register(Product)

# Register your models here.
