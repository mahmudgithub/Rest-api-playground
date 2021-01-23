from django.shortcuts import render
from rest_framework import generics
from.models import one
from.serializers import OneSerializer

class OneViews(generics.ListAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer
