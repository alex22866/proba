
from django.contrib import admin
from django.urls import path, include
from .views import HeaderView, HeaderdisView

urlpatterns = [
    path('head/', HeaderView.as_view(), name='head'),
    path('headdis/',HeaderdisView.as_view(), name='headdis'),
]
