from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from . models import Info
from . serializer import InfoSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404



class InfoViewset(viewsets.ViewSet ):
    def list(self, request):
        obj_data = Info.objects.all()
        serializer = InfoSerializers(obj_data, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InfoSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Info.objects.all()
        obj_data = get_object_or_404(queryset, pk=pk)
        serializer = InfoSerializers(obj_data)
        return Response(serializer.data)

    def update(self, request, pk=None):
        obj_data= Info.objects.get(pk=pk)
        serializer = InfoSerializers(obj_data, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

