from rest_framework import generics
from django.shortcuts import render, redirect
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

#Serializers
class CswList(generics.CreateAPIView):
    serializer_class = CswSerializer         
    queryset = Person.objects.all()
    def get_queryset(self):

        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class CswDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = CswSerializer

class Work_contactList(generics.CreateAPIView):
    serializer_class = Work_contactSerializer    
    queryset = Work_contact.objects.all()
    def get_queryset(self):

        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class Work_contactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work_contact.objects.all()
    serializer_class = Work_contactSerializer

class CustomerList(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Contact.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = CustomerSerializer
    
class education_and_trainingList(generics.CreateAPIView):
    serializer_class = education_and_trainingSerializer
    queryset = education_and_training.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class education_and_trainingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = education_and_training.objects.all()
    serializer_class = education_and_trainingSerializer

class pst_five_workList(generics.CreateAPIView):
    serializer_class = pst_five_workSerializer
    queryset = pst_five_work.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class pst_five_workDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pst_five_work.objects.all()
    serializer_class = pst_five_workSerializer

class practise_outsideList(generics.CreateAPIView):
    serializer_class = practise_outsideSerializer
    queryset = practise_outside.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class practise_outsideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = practise_outside.objects.all()
    serializer_class = practise_outsideSerializer

class character_refList(generics.CreateAPIView):
    serializer_class = character_refSerializer
    queryset = character_ref.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class character_refDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = character_ref.objects.all()
    serializer_class = character_refSerializer

class rivate_practiceList(generics.CreateAPIView):
    serializer_class = rivate_practiceSerializer
    queryset = rivate_practice.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class rivate_practiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = rivate_practice.objects.all()
    serializer_class = rivate_practiceSerializer

class UserList(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def get_queryset(self):

        
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer