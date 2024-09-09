from django.contrib import admin
from django.urls import path, include
from flashcard import views

urlpatterns = [
   path("", views.index, name="flashcard"),
   path("card/<int:cardset_id>", views.card, name="flashcard_card"),
   path("study/<int:cardset_id>", views.study, name="flashcard_study"),
]