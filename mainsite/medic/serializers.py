from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse_lazy
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.HyperlinkedModelSerializer):
    medicines = serializers.HyperlinkedRelatedField(many=True, queryset=Medicine.objects.all(), view_name='medic:medicine_info')

    class Meta:
        model = User
        fields = ['id', 'username', 'medicines']

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name','phone_no','password']

    def validate(self, data):
        if data['name'] == data['password'] or len(data['password']) <= 5:
            raise serializers.ValidationError('Invalid Password: password must not same as name and must be minimum 5 character in length.')
        else:
            return data

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['name', 'price', 'number_of_beds']

class MedicineSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Medicine
        fields = ['name', 'company', 'owner']

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    treated_by = DoctorSerializer(many=True, read_only=True)
    prescribed = MedicineSerializer(many=True, read_only=True)
    ward = WardSerializer(read_only=True)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = Patient
        fields = ['name', 'phone_no','photo','password','treated_by','ward','date_admitted','prescribed']
        validators = [
            UniqueTogetherValidator(
                queryset=Patient.objects.all(),
                fields=['name', 'phone_no'],
                message='Patient With same number is already registered'
            )
        ]





