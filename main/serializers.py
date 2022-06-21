from rest_framework import serializers
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from main.models import Member, User

from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email', 'password', 'is_active', 'created', 'updated']

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    member = serializers.ReadOnlyField(source='member.username')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Member
        fields = ['url','member' 'member_number', 'address','date_of_birth', 'age',
                  'gender','national_id','nationality'
                  ]
        read_only_fields = ['age', 'member_number']
