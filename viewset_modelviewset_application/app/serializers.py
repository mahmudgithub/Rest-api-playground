from rest_framework import serializers
from .models import one,two

class OneSerializer(serializers.Modelserializer):
    class Meta:
        model=one
        fields=['__all__']

class TwoSerializer(serializers.Modelserializer):
    model=two
    fields=["__all__"]