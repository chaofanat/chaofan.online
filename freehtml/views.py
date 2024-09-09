from django.shortcuts import render

# Create your views here.

from .models import compHtml
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
import json
from django.db.models import Q
from django import forms
class compHtmlForm(ModelForm):
    title= forms.CharField(label='标题', max_length=255)
    content = forms.CharField(label='Html', widget=forms.Textarea)
    extrastyle = forms.CharField(label='CSS', widget=forms.Textarea,required=False)
    extrascript = forms.CharField(label='JS', widget=forms.Textarea,required=False)

    class Meta:
        model = compHtml
        fields = ['title','content','extrastyle','extrascript']


################################################# html page ###############################################
def index(request):
    
    return render(request, 'freehtml/index.html')


def example(request,id):
    comphtml = get_object_or_404(compHtml, id=id)
    return render(request, 'freehtml/example.html', {'comphtml': comphtml})



class CompHtmlListView(ListView):
    model = compHtml
    template_name = 'freehtml/index.html'
    context_object_name = 'comphtmls'
    paginate_by = 10
    ordering = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        return queryset



class CompHtmlAdminListView(LoginRequiredMixin, ListView):
    model = compHtml
    template_name = 'freehtml/admin.html'
    context_object_name = 'comphtmls'
    paginate_by = 10
    ordering = ['title']

    def get_queryset(self):
        # 只显示当前登录用户的数据
        queryset = self.model.objects.filter(author=self.request.user).order_by(*self.ordering)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 添加额外的上下文数据
        context['user'] = self.request.user
        return context

@login_required
def comphtml_edit(request, id=None):
    instance = get_object_or_404(compHtml, id=id)
    return render(request, 'freehtml/edit.html', {'comphtml': model_to_dict(instance)})

@login_required
def comphtml_new(request):
    return render(request, 'freehtml/edit.html')






######################################################### api ###############################################
@login_required
def comphtml_create(request):
    try:
        if request.method == 'POST':
            # 解析post提交的json数据
            data = json.loads(request.body.decode('utf-8'))
            form = compHtmlForm(data)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()

                #将instance转为json格式返回
                data = model_to_dict(instance)
                return JsonResponse({'message': 'success', 'data': data}, status=201)
            else:
                errors = form.errors.as_json()
                return JsonResponse({'message': 'error', 'detail': errors}, status=400)
        else:
            return JsonResponse({'message': 'error', 'detail': 'Only POST requests are allowed.'}, status=405)
    except Exception as e:
        return JsonResponse({'message': 'error', 'detail': str(e)}, status=500)
        

@login_required
def comphtml_delete(request, id):
    try:
        if request.method == 'POST':
            # 使用 get_object_or_404 处理对象不存在的情况
            instance = get_object_or_404(compHtml, id=id)
            if instance.author != request.user:
                return JsonResponse({'message': 'error', 'detail': 'You do not have permission to delete this object.'}, status=403)
            instance.delete()
            return JsonResponse({'message': 'success'}, status=200)
        else:
            return JsonResponse({'message': 'error', 'detail': 'Only POST requests are allowed.'}, status=405)
    except Exception as e:
        return JsonResponse({'message': 'error', 'detail': str(e)}, status=500)


@login_required
def comphtml_update(request, id):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            instance = get_object_or_404(compHtml, id=id)
            form = compHtmlForm(data, instance=instance)
            if instance.author != request.user:
                return JsonResponse({'message': 'error', 'detail': 'You do not have permission to update this object.'}, status=403)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'success', 'data': form.cleaned_data}, status=200)
            else:
                errors = form.errors.as_json()
                return JsonResponse({'message': 'error', 'detail': errors}, status=400)
        else:
            return JsonResponse({'message': 'error', 'detail': 'Only POST requests are allowed.'}, status=405)
    except compHtml.DoesNotExist:
        return JsonResponse({'message': 'error', 'detail': 'Object not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'message': 'error', 'detail': str(e)}, status=500)

        



