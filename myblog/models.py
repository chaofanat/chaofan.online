from django.db import models

# Create your models here.
#导入用户模型
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

from django.urls import reverse  
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    def tagtoblog(self):
        return Blog.objects.filter(tags=self)


    from django.db.models import QuerySet
    def get_blogs_by_tag(self) -> QuerySet[any]:
        """
        根据当前标签反查所有关联的博客。
        
        返回:
            与当前标签关联的所有博客的QuerySet。
        """
        return Blog.objects.filter(tags=self)
    
    def get_absolute_url(self):
        return reverse('myblog:category', kwargs={'pk': self.pk})
    

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.CharField(max_length=100)  # slug,三到5个单词高度概括文章内容，-连接，小写字母
    time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='myblog/assets/img', default='')
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=200,null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    #阅读统计
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
#置顶博客
class FeaturedBlog(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    #展示类型：轮播展示、全站首位展示、全站普通展示、分类首位展示、分类普通展示
    type_options = (
        ('carousel', '轮播展示'),
        ('all-top', '全站首位展示'),
        ('all-normal', '全站普通展示'),
        ('category-top', '分类首位展示'),
        ('category-normal', '分类普通展示'),
    )

    #全站置顶只允许一个，分类置顶每个分类只能一个
    type = models.CharField(max_length=20, choices=type_options, default='all')
    def __str__(self):
        return self.blog.title
    



    


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} -> {self.email}'
    
    class Meta:
        ordering = ['-time']
        verbose_name = "留言"
        verbose_name_plural = "留言"