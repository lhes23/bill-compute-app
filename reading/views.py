from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from reading.models import House, Reading, Tenant, YearlyBill
from reading.serializers import HouseSerializer, ReadingSerializer, TenantSerializer,YearlyBillSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class =  ReadingSerializer
    
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    
    @api_view(["GET"])
    def getActive(requests):
        query = Tenant.objects.filter(is_active=True)
        serializer = TenantSerializer(query, many=True)
        # return Response({"tenants": serializer.data})
        return Response(serializer.data)
    
class YearlyBillViewSet(viewsets.ModelViewSet):
    queryset = YearlyBill.objects.all()
    serializer_class = YearlyBillSerializer