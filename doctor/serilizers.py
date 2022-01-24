from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {
                'password': {'write_only': True},
                'username': {'read_only': True}
            }

class DoctorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['username','password']


