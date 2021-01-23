from django.shortcuts import render
from rest_framework import generics
from .serializers import OneSerializer
from .models import one

class OneViews(generics.CreateAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer