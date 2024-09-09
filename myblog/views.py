from django.shortcuts import render, HttpResponse
from myblog.models import Blog,Contact,FeaturedBlog,Category,Tag
import math

# Create your views here.
def index(request):
    #趋势：博客按阅读量排序取前5
    trend =  Blog.objects.all().order_by('-views')[:5]
    featuredblog = FeaturedBlog.objects.all()
    all_normal_featuredblog = FeaturedBlog.objects.filter(type='all-normal')
    
    tag = Tag.objects.all()
    categorytop = FeaturedBlog.objects.filter(type='category-top').order_by('blog__category')
    categorynormal = FeaturedBlog.objects.filter(type='category-normal').order_by('blog__category')
    category = categorytop.values('blog__category').distinct()
    categoryblog = {}
    for c in category:
        categoryblog[c['blog__category']] = categorynormal.filter(blog__category=c['blog__category'])
    
    result={'featuredblog': featuredblog,'Category': category, 'Tag': tag,'TrendBlog': trend,'CategoryBlog': categoryblog,'CategoryTop': categorytop,'all_normal_featuredblog': all_normal_featuredblog}
    return render(request, 'myblog/index.html', result)


def single_post(request,id=None):
    if id:
        data = Blog.objects.filter(id=id)
        data.update(views=data[0].views+1)
        data = data[0]
        data.save()
    else :
        data = Blog.objects.all().order_by('-time')[0]
    
    trend =  Blog.objects.all().order_by('-views')[:5]
    latest = Blog.objects.all().order_by('-time')[:5]
    tag = Tag.objects.all()
    category = Category.objects.all()
    
    result={'blog': data,'TrendBlog': trend,'LatestBlog': latest,'Tag': tag,'Category': category}
    return render(request, 'myblog/single-post.html', result)


def category(request,page=1,categoryid=None):
    no_of_post=5
    
    
    page=int(page)

    if categoryid:
        blog = Blog.objects.filter(category_id=categoryid)
        category = Category.objects.filter(id=categoryid)[0]
        
    else :
        latestblog = Blog.objects.all().order_by('-time').first()
        category = latestblog.category
        blog = Blog.objects.filter(category=category)


    length=len(blog)
    no_of_page=math.ceil(length/no_of_post)
    blog=blog[(page-1)*no_of_post: page*no_of_post]
    if page>1:
        prev=page-1
    else:
        prev=None

    if page<math.ceil(length/no_of_post):
        nxt= page+1

    else:
        nxt=None
   

    trend =  Blog.objects.filter(category=category).order_by('-views')[:5]
    latest = Blog.objects.filter(category=category).order_by('-time')[:5]
    categories = Category.objects.all()
    tag = Tag.objects.all()

    result={'blog': blog, 'prev': prev, 'nxt': nxt, 'no_of_page': list(range(1,no_of_page+1)),
              'pagenumber': page,'Category': category,'TrendBlog': trend,'LatestBlog': latest,
            'categories': categories,'Tag': tag,
            }
    return render(request, 'myblog/category.html', result)

def tag(request,page=1,tagid=None):
    no_of_post=5

    page=int(page)

    if tagid:
        blog = Blog.objects.filter(tags__id=tagid)
        tag = Tag.objects.filter(id=tagid)[0]
        
    else :
        latestblog = Blog.objects.all().order_by('-time').first()
        tag = latestblog.tags.first()
        blog = Blog.objects.filter(tags=tag)
    
    length=len(blog)
    no_of_page=math.ceil(length/no_of_post)
    blog=blog[(page-1)*no_of_post: page*no_of_post]
    if page>1:
        prev=page-1
    else:
        prev=None
    
    if page<math.ceil(length/no_of_post):
        nxt= page+1
    else:
        nxt=None
    
    trend =  Blog.objects.filter(tags=tag).order_by('-views')[:5]
    latest = Blog.objects.filter(tags=tag).order_by('-time')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    result={'blog': blog, 'prev': prev, 'nxt': nxt, 'no_of_page': list(range(1,no_of_page+1)),
            'pagenumber': page,'Tag': tag,'TrendBlog': trend,'LatestBlog': latest,'Tags': tags,
            'categories': categories,
            }
    return render(request, 'myblog/tag.html', result)


import markdown
def about(request):

    #读取项目根目录文件夹下的README.md文件
    f = open('README.md', 'r', encoding='utf-8')
    content = f.read()
    f.close()
    #将其从md格式转换为html格式
    content = markdown.markdown(content)
    checkedtext = '[X]'
    checkedbox = '<input type="checkbox" checked disabled>'
    unchecktext = '[ ]'
    uncheckbox = '<input type="checkbox" disabled>'
    content = content.replace(checkedtext, checkedbox)
    content = content.replace(unchecktext, uncheckbox)

    result={'content': content}
    return render(request,'myblog/about.html', result)



    
   

def contact(request):

    context={'success':False}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=Contact(name=name, email=email, message=message)
        ins.save()
        context={'success':True}

    


    return render(request, 'myblog/contact.html', context)


# def search(request):
#     return render(request, 'myblog/search-post.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm  

from django.http import JsonResponse


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # 将表单数据保存到数据库，author字段直接从request.user获取
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            # 添加多对多关系的tags
            form.save_m2m()
            return JsonResponse({"status":"success","msg": "博客创建成功", "new_blog_id":new_blog.pk}, content_type='application/json',status=200)
            #return redirect( 'post_detail', id=new_blog.pk)  # 假设您有blog_detail的URL来显示博客详情
        
        else:
            #处理表单验证失败的情况

            return JsonResponse({"status":"error","msg": f"表单验证失败:{form.errors}"}, content_type='application/json',status=400)
    else:
        form = BlogForm()
    
        # 获取所有分类和标签供表单选择
        categories = Category.objects.all()
        tags = Tag.objects.all()
        ai_apikey = "aa"
        context = {
            'form': form,
            'categories': categories,
            'tags': tags,
            'ai_apikey': ai_apikey,
        }
        
        return render(request, 'myblog/write.html', context)

import json

def create_tag(request):
    if request.method == 'POST':
       #获取name字段
        name = request.POST.get('name', None)
        if not name:
            return HttpResponse('{"status":"error","msg":"标签名称不能为空"}', content_type='application/json',status=400)
        #判断是否已存在，若存在返回json提示错误
        if Tag.objects.filter(name=name).exists():
            return HttpResponse('{"status":"error","msg":"标签已存在"}', content_type='application/json',status=400)
        else:
            #若不存在则添加至数据库
            tag = Tag(name=name)
            tag.save()
            #返回data
            data = {
                'id': tag.id,
                'name': tag.name,
            }
            return HttpResponse(json.dumps(data), content_type='application/json',status=200)

    
    else:
        return HttpResponse('{"status":"error","msg":"请求方式错误"}', content_type='application/json',status=400)
       


def create_category(request):
    if request.method == 'POST':
       #获取name字段
        name = request.POST.get('name', None)
        if not name:
            return HttpResponse('{"status":"error","msg":"分类名称不能为空"}', content_type='application/json',status=400)
        #判断是否已存在，若存在返回json提示错误
        if Category.objects.filter(name=name).exists():
            return HttpResponse('{"status":"error","msg":"分类已存在"}', content_type='application/json',status=400)
        else:
            #若不存在则添加至数据库
            category = Category(name=name)
            category.save()
            #返回data
            data = {
                'id': category.id,
                'name': category.name,
            }
            return HttpResponse(json.dumps(data), content_type='application/json',status=200)

    
    else:
        return HttpResponse('{"status":"error","msg":"请求方式错误"}', content_type='application/json',status=400)
    




def leave_message(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        if not name or not email or not message:
            return HttpResponse('{"status":"error","msg":"留言内容不能为空"}', content_type='application/json',status=400)
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return HttpResponse('{"status":"success","msg":"留言成功"}', content_type='application/json',status=200)