# content/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('test', test.as_view(), name='test'),  # http://localhost:8000/content/test 경로로 접근
    # path('aaa', func.as_view(), name='aaa'),  # 8000/content/aaa 경로, func 함수 실행
]
