from django.shortcuts import render
from rest_framework import generics
from .models import one,two
from .serializers import OneSerializer,TwoSerializer

class OneViews(generics.ListCreateAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer

class TwoViews(generics.RetrieveUpdateDestroyAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer




class ThreeViews(generics.ListCreateAPIView):
    queryset=two.objects.all()
    serializer_class=TwoSerializer

class FourViews(generics.RetrieveUpdateDestroyAPIView):
    queryset=two.objects.all()
    serializer_class=TwoSerializer