from django.urls import path
from django.urls import path
from . import views 
from main_app.views import *


urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session/<pk>/'),
    path('product', Product.as_view(), name='product'),
    path('cancel', views.cancel, name='cancel'),
    path('success', views.success, name='success'),
    ]