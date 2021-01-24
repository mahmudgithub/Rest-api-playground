from django.shortcuts import render
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
from .models import one,two
from .serializers import OneSerializer,TwoSerializer



class OneViews(generics.ListCreateAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [IsAdminUser]
    
class TwoViews(generics.RetrieveUpdateDestroyAPIView):
    queryset=one.objects.all()
    serializer_class=OneSerializer
def get_object(self):
    obj = get_object_or_404(self.get_queryset())
    self.check_object_permissions(self.request, obj)
    return obj




class ThreeViews(generics.ListCreateAPIView):
    queryset=two.objects.all()
    serializer_class=TwoSerializer

class FourViews(generics.RetrieveUpdateDestroyAPIView):
    queryset=two.objects.all()
    serializer_class=TwoSerializer