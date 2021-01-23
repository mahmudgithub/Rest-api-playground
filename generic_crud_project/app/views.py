from django.shortcuts import render
from rest_framework import generics
from .models import one,two
from .serializers import OneSerializer,TwoSerializer

class OneViews(generics.ListCreateAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer

class OneViews(generics.RetrieveUpdateDestroyAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer