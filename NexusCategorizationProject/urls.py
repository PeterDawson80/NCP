"""NexusCategorizationProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import text_query.views
import customer_relationship_management.views

urlpatterns = [
    path('',text_query.views.Home, name='home'),
    path('contact/',text_query.views.Contact, name='contact'),
    path('count/',text_query.views.count, name='count'),
    path('admin/', admin.site.urls),
    path('dashboard/',customer_relationship_management.views.Dashboard, name='dashboard'),
    path('dashboard/<int:query_id>/', customer_relationship_management.views.detail, name='query_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
