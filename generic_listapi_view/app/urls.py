from django.urls import path
from.views import *

urlpatterns = [
    path('api/',OneViews.as_view(),name='home')
]