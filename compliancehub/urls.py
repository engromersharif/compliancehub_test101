"""
URL configuration for compliancehub project.

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
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.generic import TemplateView

# Up two folders to serve "docs" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(BASE_DIR, 'docs')

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('jhpl-ims/', include('jhpl_ims.urls')),
    path('ajcl-ims/', include('ajcl_ims.urls')),
    path("admin/", admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^docs/(?P<path>.*)$', serve,
            {'document_root': DOCS_ROOT, 'show_indexes': True},
            name='docs_path'
            ),

]
