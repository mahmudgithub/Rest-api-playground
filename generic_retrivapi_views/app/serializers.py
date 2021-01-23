from rest_framework import serializers
from.models import one

class OneSerializers(serializers.ModelSerializer):
    class Meta:
        model=one
        fields='__all__'