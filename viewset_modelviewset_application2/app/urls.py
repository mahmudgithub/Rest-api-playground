from django.urls import path,include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'api1', views.OneViewset, basename='one')
router.register(r'api2', views.TwoViewset, basename='two')

urlpatterns = [
    path("api/",include(router.urls))
    
]
