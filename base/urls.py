"""
URL configuration for base project.

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
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views
from home.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', logout_view, name='logout'),
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api/v1/userslist/', UsersViewSet.as_view({'get': 'list'})),
    # path('api/v1/userslist/<int:pk>', UsersViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
