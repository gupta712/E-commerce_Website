from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer,Cart,OrderPlaced,Product
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(OrderPlaced)
admin.site.register(Product)

# Register your models here.
