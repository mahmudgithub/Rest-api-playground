from django.urls import path
from.views import OneViews,TwoViews,ThreeViews,FourViews

urlpatterns = [
    path('api1/',OneViews.as_view(),name='home1'),
    path('api1/<int:pk>/',TwoViews.as_view(),name='home2'),
    path('api2/',ThreeViews.as_view(),name='home3'),
    path('api2/<int:pk>/',FourViews.as_view(),name='home4')
]
