from rest_framework import serializers
from.models import one


class OneSerilizer(serializers.ModelSerializer):
    class Meta:
        model=one
        fields='__all__'