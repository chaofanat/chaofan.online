"""
URL configuration for  project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", include(("appUser.urls","appUser"), namespace="appUser")),
    path('accounts/', include('allauth.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    path('silk/', include('silk.urls', namespace='silk')),
    path("", include(("appIndex.urls","appIndex"), namespace="appIndex"))
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

#add myblog app
urlpatterns += [
    path('myblog/', include('myblog.urls')),
]

#add flashcard app
urlpatterns += [
    path('flashcard/', include('flashcard.urls')),
]

#add freehtml app
urlpatterns += [
    path('freehtml/', include('freehtml.urls')),
]

#add objectstorage app
urlpatterns += [
    path('objectstorage/', include('appObjectStorage.urls')),
]


#ninjia api
from .apis import api_session
from .apis_v1 import api as api_v1
urlpatterns += [
    path('api/v1/', api_v1.urls),
    path('api/', api_session.urls),
]