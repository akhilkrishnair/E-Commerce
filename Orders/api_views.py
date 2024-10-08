from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Orders,OrderAddress
import json
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from Cart.models import Cart
from rest_framework.decorators import action


class OrderView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):

        if self.request.query_params.get('orderId'):
            order_id = self.request.query_params.get('orderId')
            data = None
            try:
                data = Orders.objects.get(id=order_id)
            except Orders.DoesNotExist:  
                data = {"message":"object does not found"}  
            return [data]

        if self.request.query_params.get('order_id'):
            order_id = self.request.query_params.get('order_id')
            order = Orders.objects.get(id=order_id)
            order.status = "Cancelled"
            order.save()
            order_list = []
            order_list.append(order)
            return order_list
        user = self.request.user

        return Orders.objects.filter(user=user).order_by('-ordered_date').select_related(
            'user',
            'product_variant__product_color_variant__product__category',
            'product_variant__product_color_variant__product__brand',
            'product_variant__product_color_variant__product',
            'product_variant__product_color_variant',
            'product_variant__size',
            'product_variant',
            'order_address',
            'payment'
        )



class OrderAddressView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderAddressSerializer
    
    def get_queryset(self):
        user = self.request.user
        return OrderAddress.objects.filter(user=user)
    


class OrderConfirmView(APIView):
    permission_classes = (IsAuthenticated,) 

    def put(self,request):
        cart_payment = request.data['cart_payment']           
        serializer = OrderConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart_payment)
            return Response({'message':"order successfully created"},status=status.HTTP_200_OK)
        return Response(serializer.errors)



# razorpay payment handler
import razorpay
from rest_framework.decorators import api_view
MAX_AMOUNT = 500000

@api_view(['POST'])
def initiate_payment(request):
    if request.method == 'POST':
        user = request.user
        amount =  0
        order_address_id = request.data['order_address_id']
        cart = Cart.objects.filter(user=user)

        for c in cart:
            amount += (c.quantity * c.product_variant.selling_price())

        amount *= 100

        if amount > MAX_AMOUNT*100:
            return Response({'message':"Your transaction limit is Rs.500000"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        cart_payment = order_save(user, cart, order_address_id )
        if isinstance(cart_payment, str):
            return Response({'message':cart_payment}, status=status.HTTP_404_NOT_FOUND)
       
        client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
                
        payment_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
        }

        order = client.order.create(data=payment_data)

        user_details = {
            'email':user.email,
            'full_name': f'{user.first_name} {user.last_name}',
        }

        user_json = json.dumps(user_details)
        data = {
            "razor_order":order,
            "cart_payment":cart_payment,
            "user":user_json
        }
        return Response(data, status=status.HTTP_200_OK)



class CashOnDeliveryView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashOnDeliverySerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"order success"})
        



def order_save(*args):
    user = args[0]
    cart = args[1]
    order_address_id = args[2]
    cart_id = []
    payment_id = []

    order_address = OrderAddress.objects.get(id=order_address_id)
    with transaction.atomic():
        for c in cart:
            try:
                product_variant = ProductVariant.objects.get(id=c.product_variant.pk)
                if product_variant.stock < c.quantity:
                    return "stock_error"
            except product_variant.DoesNotExist:
                return "obj_error"
            
            payment = Payment.objects.create(
                user = user,
                price_paid = c.product_variant.selling_price(),
                payment_mode = "RazorPay" ,
                razorpay_payment_status = "pending"
            )
            
            
            order = Orders.objects.create(
                user=user,
                order_address = order_address,
                product_variant = c.product_variant,
                price_was = c.product_variant.selling_price(),
                quantiy_was = c.quantity,
                payment = payment
            )
            order.order_id = "e-shop-"+ str(order.order_id)
            
            product_variant.stock -= c.quantity
            product_variant.save()

            payment.save()
            order.save()
            payment_id.append(payment.pk)
            cart_id.append(c.pk)
    
    cart_payment = {"cart_id":cart_id,"payment_id":payment_id}
    return cart_payment
            


@api_view(['POST'])
def razorpay_payment_failure(request):

    payment_ids = request.data['payment_id']

    for index in range(len(payment_ids)):
        payment = Payment.objects.get(id = payment_ids[index])
        order = payment.orders_set.first()
        quantity_was = order.quantiy_was

        product_variant_obj = order.product_variant
        product_variant_obj.stock += quantity_was
        product_variant_obj.save()
        
        order.delete()
        payment.delete()     
    
    return Response({"message":"payment fail successfully handled"}, status=status.HTTP_200_OK)