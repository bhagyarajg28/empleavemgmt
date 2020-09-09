"""empleavemgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app1 import views
from django.conf.urls import url
urlpatterns = [
   path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^signup$', views.registration, name="registration"),
    url(r'^login$', views.loginn, name="loginn"),
    url(r'^manager$', views.manager, name="manager"),
    url(r'^employee$',views.employee,name='employee'),
    url(r'^logout$',views.logout_view,name='logout_view'),
    url(r'^leave/(?P<t>\d+)$',views.leave,name='leave'),
    url(r'^status$',views.status,name='status')
]
