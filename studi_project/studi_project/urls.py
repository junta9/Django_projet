"""
URL configuration for studi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from postgres.views import index, catalog, search, promotion, category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('promotion/', promotion, name='promotion'),
    path('search/', search, name='search'),
    path('category/', category, name='category'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
