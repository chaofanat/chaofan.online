
"""
URL configuration for app ObjectStorage project.
"""
from django.urls import path

from .views import  FileManagementView

urlpatterns = [
    path('', FileManagementView.as_view(), name='file-management'),
]