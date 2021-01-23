from django.urls import path
from.views import OneViews

urlpatterns = [

    path('api/<int:pk>/',OneViews.as_view(),name='home')
]
