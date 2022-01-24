import imp
from django.shortcuts import render
from rest_framework.views import APIView
from .serilaizers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Patients as Patient


# Create your views here.

class Patients(APIView):

    def post(self, request):
        serilaizer = PatientSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)

        return Response(serilaizer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        patients= Patient.objects.all()
        serilaizers= PatientSerializer(patients,many=True )
        return Response(serilaizers.data)

    # def get(self,request,pk):
    #     patient = Patient.objects.get(id = pk)
    #     serilaizer = PatientSerializer(patient)
    #     return Response(serilaizer.data)

