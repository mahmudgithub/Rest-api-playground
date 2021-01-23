from rest_framework import serializers
from.models import one

class OneSerializer(serializers.ModelSerializer):
    class Meta:
        model=one
        fields='__all__'