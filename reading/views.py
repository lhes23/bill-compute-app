from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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
    
    # @api_view(["GET"])
    # def getActive(requests):
    #     query = Tenant.objects.filter(is_active=True)
    #     serializer = TenantSerializer(query, many=True)
    #     return Response(serializer.data)
    
            
    @api_view(["GET","POST"])
    def getActive(request):
        match(request.method):
            case "GET":
                query = Tenant.objects.filter(is_active=True)
                serializer = TenantSerializer(query, many=True)
                return Response(serializer.data)
            case "POST":
                serializer = TenantSerializer(data=request.data)
                if serializer.is_valid():
                    house_id = serializer.validated_data["house_id"]
                    tenants = Tenant.objects.filter(house_id=house_id)
                    for t in tenants:
                        t.is_active = False
                        t.save()
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class YearlyBillViewSet(viewsets.ModelViewSet):
    queryset = YearlyBill.objects.all()
    serializer_class = YearlyBillSerializer