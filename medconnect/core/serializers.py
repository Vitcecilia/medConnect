from rest_framework import serializers

from core import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class TelephoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class HealthInsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class Blood_TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class PatientHealthInsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class MedicSerializers(serializers.ModelSerializer):
            class Meta:
                model = models.Telephone
                fields = '__all__'

class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class ConsultationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class MedicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class MedicationConsultationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'