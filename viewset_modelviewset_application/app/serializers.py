from rest_framework import serializers
from .models import one,two
# from .models import *

class OneSerializer(serializers.ModelSerializer):
    class Meta:
        model=one
        fields='__all__'

class TwoSerializer(serializers.ModelSerializer):
    class Meta:
        model=two
        fields='__all__'