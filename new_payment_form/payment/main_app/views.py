from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import *
import stripe


stripe.api_key = 'sk_test_51M78snLo83VUKO2XyBmevW4WlKSTaoYOId5UPo5D9Tx6xbLB4GIxgdwMSsx8kxTa7NGCMtWjVc5m4viPFR0Pj6qY00pSYfI6U3'


class CreateCheckoutSessionView(TemplateView):
    # Session creation
    def dispatch(self, request, *args, **kwargs):
        need_item = Item.objects.get(id=6)
        resp_checkout_session = stripe.checkout.Session.create(success_url='http://127.0.0.1:8000/main_app/success',
                                                                cancel_url='http://127.0.0.1:8000/main_app/cancel',
        line_items=[
                {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': need_item.price,
                    'product_data': {
                        'name': need_item.name,
                    },
                },
                'quantity': 1,
                },
            ],
        mode='payment'
        )
        return JsonResponse({'id': resp_checkout_session.id})


class Product(TemplateView):
    # Product page
    def dispatch(self, request, *args, **kwargs):
        need_item = Item.objects.get(name='Xiaomi – Mi TV 4A 32 (Телевизор)')
        return render(request,'main_app/index.html', {'product':need_item})


def cancel(request):
    # Payment cancel Page
    return render(request,'main_app/cancel.html')


def success(request):
    # Payment success page
    return render(request,'main_app/success.html')