from django.shortcuts import render
from APIapp.models import APIModel
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from APIapp.serializers import APIappSerializers
from rest_framework import status, viewsets


# Create your views here.
class IndexViewSet(viewsets.ModelViewSet):

    serializer_class = APIappSerializers
    queryset = APIModel.objects.all()