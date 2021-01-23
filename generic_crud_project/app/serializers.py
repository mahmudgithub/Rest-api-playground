from rest_framework import serializers
from .models import one,two

class OneSerializer(serializers.ModelSerializer):
    class Meta:
        models=one
        fields='__all__'

class TwoSerializer(serializers.ModelSerializer):
    class Meta:
        model=two
        fields='__all__'
    