from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    # home page
    path('', home, name='home'),
    
    # user page 
    path('user', userPage, name='user-page'),
    path('account/', accountSettings, name="account"),
    
    # data page
    path('customer/<str:pk>/', customer, name='customer'),
    path('products/', product, name='product'),
    
    # orders page
    path('create_order/<str:pk>/', createOrder, name="create_order"),
    path('update_order/<str:pk>', updateOrder, name="update_order"),
    path('delete_order/<str:pk>', deleteOrder, name="delete_order"),
    
    # auth page
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    
    # change password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]