from django.urls import path, include
from rest_framework import routers

from .views import RessultView

app_name = 'whiskeys'

urlpatterns = [
    path('result', RessultView.as_view(), name='result'),
]
