"""OrganizerApp URL Configuration

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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from OrganizerApp import views
from django.conf.urls import include
import notifications.urls

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^index/$', views.SampleView.as_view(), name='index'),
    url(r'^home/$', views.HomePageView.as_view(), name='home'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    #url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
