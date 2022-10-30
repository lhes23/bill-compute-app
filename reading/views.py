from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from reading.models import Reading
from reading.serializers import ReadingSerializer

# @api_view(["GET"])
# def getAllReadings(request):
#     return Response({"hello":"world"})

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class =  ReadingSerializer