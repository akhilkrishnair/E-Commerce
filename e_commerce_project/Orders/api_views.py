from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .serializers import OrderSerializer,OrderAddressSerializer
from .models import Orders,OrderAddress


class OrderView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Orders.objects.filter(user=user)



class OrderAddressView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = OrderAddressSerializer
    
    def get_queryset(self):
        user = self.request.user
        return OrderAddress.objects.filter(user=user)
    


class OrderConfirmView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

