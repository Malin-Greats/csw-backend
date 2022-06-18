from rest_framework import serializers
from .models import Person, Contact, Work_contact, education_and_training, pst_five_work, character_ref, practise_outside, rivate_practice
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CswSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')

class Work_contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_contact
        fields = ('__all__')

class education_and_trainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_and_training
        fields = ('__all__')

class pst_five_workSerializer(serializers.ModelSerializer):
    class Meta:
        model = pst_five_work
        fields = ('__all__')

class practise_outsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = practise_outside
        fields = ('__all__')

class character_refSerializer(serializers.ModelSerializer):
    class Meta:
        model = character_ref
        fields = ('__all__')

class rivate_practiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = rivate_practice
        fields = ('__all__')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email',  'password']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user


