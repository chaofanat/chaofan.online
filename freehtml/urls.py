'''
app:freehtml
urls.py
URL Configuration
'''
from django.urls import path

from .views import CompHtmlListView, comphtml_create, comphtml_update, comphtml_delete, example,CompHtmlAdminListView,comphtml_edit,comphtml_new

urlpatterns = [
    # freehtml
    path('', CompHtmlListView.as_view(), name='comphtml-list'),
    path('admin/', CompHtmlAdminListView.as_view() , name='comphtml-admin-list'),
    path('example/<int:id>/', example, name='comphtml-example'),
    path('edit/<int:id>/' , comphtml_edit, name='comphtml-edit'),
    path('new/', comphtml_new, name='comphtml-new'),

    # freehtml api
    path('create/', comphtml_create, name='comphtml-create'),
    path('update/<int:id>/', comphtml_update, name='comphtml-update'),
    path('delete/<int:id>/', comphtml_delete, name='comphtml-delete'),
    
    
]