from django.urls import path
from . import views


urlpatterns = [
    path('order-confirm/',views.order_confirm, name='order-confirm'),
    path('address_creation/',views.address_creation, name='address_creation'),
    path('paypal_payment/(?P<cart_items>\w+)',views.paypal_payment_success, name='payment-success'),
    path('paypal_payment_f/(?P<cart_items_f>\w+)',views.paypal_payment_success, name='payment-fail'),
    path('razorpay_success/(?P<user>\w+)', views.razorpay_payment_success, name='razorpay-success'),
    path('cash-on-delivery/',views.cash_on_delivery, name='cash-on-delivery'),
    path('orders/',views.all_orders, name='all-orders'),
    path('order-details/<str:order_id>/',views.order_detail, name='order-details'),
]