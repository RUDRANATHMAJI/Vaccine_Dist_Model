"""SiCoViDis URL Configuration

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
from django.urls import path, include
from home_page.views import home
from sir.views import sir
from vaccine.views import vaccine

urlpatterns = [
	path('',home,name = 'home'),
	path('sir/',sir,name = 'sir'),
    path('admin/', admin.site.urls),
    path('sir/', include('sir.urls', namespace='sir')),
    path('vaccine/', include('vaccine.urls', namespace='vaccine')),
	path('vaccine/',vaccine,name = 'vaccine'),
    #path('admin/', admin.site.urls),
]



