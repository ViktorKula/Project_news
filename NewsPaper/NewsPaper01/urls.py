"""
URL configuration for NewsPaper01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from news.views import *

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'articles', ArticlesViewSet, basename='articles')

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),  # Оставили только allauth
    path('news/', include('news.urls')),
    path('articles/', include('news.urls')),
    path('', include('news.urls')),
    path('api/', include(router.urls)),


    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # подключались к главному приложению с префиксом products/.

]
