from django.shortcuts import render
from rest_framework import viewsets
# from .serializers import OneSerializer
# from .serializers import TwoSerializer
from .serializers import OneSerializer,TwoSerializer
# from .serializers import *
from .models import one,two
# from .models import *


class OneViewset(viewsets.ModelViewSet):
    queryset=one.objects.all()
    serializer_class = OneSerializer

class TwoViewset(viewsets.ModelViewSet):
    queryset=two.objects.all()
    serializer_class= TwoSerializer


