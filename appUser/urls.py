from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path("",views.profile,name="profile"),
    path("edit/",views.profile_edit,name="profile_edit"),

]

