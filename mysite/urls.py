"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    # path('', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^account/', include('account.urls', namespace='account')),
    # 第三方应用重置密码
    url(r'^password_reset/', include('password_reset.urls', namespace='password_reset')),
    url(r'^article/', include('article.urls', namespace='article')),
    url(r'^home/', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^image/', include('image.urls', namespace='image')),
    url(r'^course/', include('course.urls', namespace='course')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)