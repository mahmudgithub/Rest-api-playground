from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OneSerializer,TwoSerializer
from .models import one,two


class OneViewset(viewsets.ModelViewset):
    queryset=one.objects.all()
    serializer_class = serializers.OneSerializer

class TwoViewset(viewsets.ModelViewset):
    queryset=two.objects.all()
    serializer_class=serializers.TwoSerializer
