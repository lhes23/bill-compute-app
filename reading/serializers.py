from rest_framework import serializers
from .models import Reading,Tenant, House

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = "__all__"
        
class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"