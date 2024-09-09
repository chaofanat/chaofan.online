from django import forms
from .models import Blog, Category, Tag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'slug', 'category', 'image', 'summary', 'tags']
        
    # 自定义字段属性，例如添加CSS类或自定义标签
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': '请输入博客标题'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 10, 'placeholder': '开始撰写您的博客内容...'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control', 'placeholder': '请使用短横线分隔的关键词'})
        self.fields['category'].empty_label = "请选择类别"
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': '简短概述您的博客'})
        self.fields['tags'].widget.attrs.update({'class': 'form-select'})




# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag  # 指定关联的模型
#         fields = ['name'] 


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category  # 指定关联的模型
#         fields = ['name']