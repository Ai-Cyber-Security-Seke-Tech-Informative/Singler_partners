"""
URL configuration for singler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #  Authentication & Registration (email + social)
    path('auth/', include('dj_rest_auth.urls')),  # login, logout, password reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # email registration
    path('auth/social/', include('allauth.socialaccount.urls')),  # Google, Facebook, GitHub login endpoints

    #  Your app endpoints (auth, join, etc.)
    path('', include('auth_app.urls')),
    path('join/', include('join_app.urls')),
    path('partner/', include('partner_app.urls')),
    path('feedback/', include('feedback_app.urls')),
    path('contact/', include('contact_app.urls')),
    path('comm/', include('comm_app.urls')),
    path('logs/', include('logs_app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)