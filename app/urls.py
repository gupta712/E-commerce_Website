from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from.forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
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
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.Customer_Profile_View.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('view_profile',views.view_profile,name='view_profile'),
    
    
    path('checkout/', views.checkout, name='checkout'),
]
