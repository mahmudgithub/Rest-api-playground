from django.urls import path
from.views import OneViews

urlpatterns = [
    path('api/',OneViews.as_view(),name='home')
]