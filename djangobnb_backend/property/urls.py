from django.urls import path
from . import api

urlpatterns = [
    path('', api.properties_list, name='property-list'),
]