from django.shortcuts import render
from rest_framework.views import APIView
from .serilizers import DoctorSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor as Doc


# Create your views here.

class Doctor(APIView):

    def get(self, format=None):
        snippets = Doc.objects.all()
        serializer = DoctorSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    