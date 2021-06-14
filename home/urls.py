from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup.html', views.signupUser, name='signup'),
    path('payment', views.payment, name='payment'),
    path('admin', admin.site.urls, name='admin'),
    path('delete', views.cancel_ticket, name='delete'),
    path('Order-History', views.Order_History, name='Order-History'),
    path('login', views.loginUser, name='login'),

   ]
