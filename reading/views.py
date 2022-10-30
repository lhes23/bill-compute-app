from django.shortcuts import render
from rest_framework import viewsets

from reading.models import House, Reading, Tenant
from reading.serializers import HouseSerializer, ReadingSerializer, TenantSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class =  ReadingSerializer
    
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer