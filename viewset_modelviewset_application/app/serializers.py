from rest_framework import serializers
from .models import *

class OneSerializer(serializers.ModelSerializer):
    class Meta:
        model=one
        fields='__all__'

class TwoSerializer(serializers.ModelSerializer):
    model=two
    fields="__all__"