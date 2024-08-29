"""
URL configuration for kinsta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from content.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sub.as_view(), name='index'),
    path('main/', main.as_view(), name='main'),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
]


# media 폴더에 접근하기 위한 코드
from django.conf import settings
from django.conf.urls.static import static
# from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
