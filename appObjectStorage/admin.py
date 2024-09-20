from django.contrib import admin

# Register your models here.
from .models import StoredFile


class StoredFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'description', 'file_type', 'size','bucket', 'tags', 'last_modified' ,'user','is_deleted')
    list_filter = ('file_type', 'tags', 'is_deleted' ,'bucket')
    search_fields = ('filename', 'description', 'tags','bucket')
    ordering = ('-last_modified',)
    readonly_fields = ('upload_time', 'last_modified', 'size' ,'user')


admin.site.register(StoredFile, StoredFileAdmin)
