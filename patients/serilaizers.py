from rest_framework import serializers
from .models import Patients
from rest_framework.authtoken.models import Token


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['name','email','password','phone','patient_id']
        extra_kwargs = {
                'password': {'write_only': True},
            }

    def create(self, validated_data):
        patient = Patients.objects.create(**validated_data)
        Token.objects.create(user=patient)

        return patient