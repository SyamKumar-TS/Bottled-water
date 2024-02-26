from django.contrib import admin
from django.urls import path
from watercanapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login_view', views.login_view, name='login_view'),
    path('logout', views.logout, name='logout'),
    path('first', views.first, name='first'),
    path('cancel_odr/<int:id>', views.cancel_odr, name='cancel_odr'),
    path('update_odr/<int:id>', views.update_odr, name='update_odr'),
    path('buy', views.buy, name='buy'),
    path('last', views.last, name='last'),
    path('company', views.company, name='company'),
    path('delivered/<int:id>', views.delivered, name='delivered'),
    path('com_odr_can/<int:id>', views.com_odr_can, name='com_odr_can'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('paymentsuccess', views.paymentsuccess, name='paymentsuccess'),
    path('updatestock', views.updatestock, name='updatestock'),
]
