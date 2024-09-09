from django.contrib import admin

# Register your models here.
from .models import FlashcardSet, Flashcard, Progress
admin.site.register(FlashcardSet)
admin.site.register(Flashcard)
admin.site.register(Progress)