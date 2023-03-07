from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICE = (
    
        ("Andhra Pradesh","Andhra Pradesh"),
        ("Andhra Pradesh","Andhra Pradesh"),
        ("Assam","Assam"),
        ("Bihar","Bihar"),
        ('Chhattisgarh','Chhattisgarh'),
        ("Goa","Goa"),
        ("Gujarat","Gujarat"),
        ('Haryana',"Haryana"),
        ('Himachal Pradesh','Himachal Pradesh'),
        ("Jammu and Kashmir",'Jammu and Kashmir'),
        ('Jharkhand','Jharkhand'),
        ('Karnataka','Karnataka'),
        ('Kerala','Kerala'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),
        ('Meghalaya','Meghalaya'),
        ('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),
        ('Odisha','Odisha'),
        ('Punjab','Punjab'),
        ('Rajasthan','Rajasthan'),
        ('Sikkim','Sikkim'),
        ('Tamil Nadu    ','Tamil Nadu'),
        ('Telangana','Telangana'),
        ('Tripura','Tripura'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Uttarakhand','Uttarakhand'),
        ('West Bengal','West Bengal ')
    
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length = 20,choices=STATE_CHOICE)
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.id)

        
CATEGORY_CHOICES = (
    
        ('M','Mobile'),
        ('L','Laptop'),
        ('TW','Top_Wear'),
        ('BW','Bottom_Wear'),
    
)

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='producting')


    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICE = (
            ('Accepted','Accepted'),
            ('Packed','Packed'),
            ('On The Way','On The Way'),
            ('Delivered','Delivered'),
            ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATE_CHOICE,default='pending')

    def __str__(self):
        return (self.id)