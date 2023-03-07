from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from.forms import LoginForm
urlpatterns = [
    path('', views.Product_view.as_view(),name ='home'),
    path('product-detail/<int:pk>', views.product_detail_view.as_view(), name='product-detail'),
    path('mobile/', views.mobile_View.as_view(), name='mobile'),
    path('mobile/<slug:data>', views.mobile_View.as_view(), name='mobiledata'),
    path('laptop/', views.laptop_View.as_view(), name='laptop'),
    path('laptopdata/<slug:data>', views.laptop_View.as_view(), name='laptopdata'),
    path('topwear/', views.top_wear_View.as_view(), name='topwear'),
    path('topweardata/<slug:data>', views.top_wear_View.as_view(), name='topweardata'),
    path('bottomwear/', views.bottom_wear_View.as_view(), name='bottomwear'),
    path('bottomweardata/<slug:data>', views.bottom_wear_View.as_view(), name='bottomweardata'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    
    
    path('checkout/', views.checkout, name='checkout'),
]
