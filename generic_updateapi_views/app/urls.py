from django.urls import path
from.views import one

urlpatterns = [
    path('api/',OneViews.as_view(),name='home')
]