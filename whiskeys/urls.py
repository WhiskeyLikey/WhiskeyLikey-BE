from django.urls import path, include
from rest_framework import routers

from .views import RessultView,NumbersView

app_name = 'whiskeys'

urlpatterns = [
    path('result', RessultView.as_view(), name='result'),
    path('number', NumbersView.as_view(), name='number'),
]
