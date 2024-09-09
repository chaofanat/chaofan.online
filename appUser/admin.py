from django.contrib import admin

# Register your models here.
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'image','website')
        }),
    )

admin.site.register(Profile,ProfileAdmin)