# content/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('test', test.as_view(), name='test'),  # http://localhost:8000/content/test 경로로 접근
]
