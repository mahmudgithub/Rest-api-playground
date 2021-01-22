from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app import views 


router = routers.DefaultRouter()
router.register(r'app1', views.OneViewset, basename='one')
router.register(r'app2', views.TwoViewset, basename='two')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))

]
