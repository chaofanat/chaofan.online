from django.contrib import admin

# Register your models here.


from .models import Blog, Contact,Category,Tag,FeaturedBlog

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'time')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('time',)


admin.site.register(Blog)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(FeaturedBlog)