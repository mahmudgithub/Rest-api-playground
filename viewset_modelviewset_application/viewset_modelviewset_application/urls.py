from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app import views
# from app.views import OneViewset,TwoViewset


router = routers.DefaultRouter()
router.register(r'api1', views.OneViewset, basename='one')
router.register(r'api2', views.TwoViewset, basename='two')

# router.register(r'api1', OneViewset, basename='one')
# router.register(r'api2', TwoViewset, basename='two')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))

]
