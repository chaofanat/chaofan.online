from django.contrib import admin
from django.urls import path, include
from myblog import views

admin.site.site_header='Hancie Phago'
admin.site.site_title="Welcome to Hancie Phago Dashboard"
admin.site.index_title="Hancie Phago Portal"


urlpatterns = [


    path('',views.index,name='blogindex'),
    path('index.html',views.index,name='blogindex'),
    path('single-post.html/<int:id>',views.single_post,name='single_post_for_single_post_page'),
    path('post-detail/<int:id>',views.single_post,name = 'post_detail'),
    path('single-post.html',views.single_post,name='single_post'),
    path('category.html',views.category,name='category'),
    path('category.html/<int:page>/<int:categoryid>',views.category,name='category_for_category_page'),
    path('category.html/<int:categoryid>',views.category,name='category_for_category'),
    path('tag.html',views.tag,name='tag'),
    path('tag.html/<int:page>/<int:tagid>',views.tag,name='tag_for_tag_page'),
    path('tag.html/<int:tagid>',views.tag,name='tag_for_tag'),
    path('blog_create.html',views.blog_create,name='blog_create'),
    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('create_tag',views.create_tag,name='create_tag'),
    path('create_category',views.create_category,name='create_category'),
    #留言post
    path('contact.html/message',views.leave_message,name='leave_message'),


]


