from django.shortcuts import render
from.models import one
from rest_framework import generics

from .serializers import OneSerializers


class OneViews(generics.RetrieveAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializers
    


