from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import  TemplateView
from .models import StoredFile
from .forms import StoredFileForm, UpdateFileForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import operator
from functools import reduce


class FileManagementView(LoginRequiredMixin, TemplateView):
    template_name = 'appObjectStorage/file_management.html'

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        files = StoredFile.objects.filter(user=request.user, is_deleted=False).order_by("-last_modified")
        
        
        if search_query:
            queries = search_query.split()
            q_objects = [Q(filename__icontains=query) for query in queries]
            query = reduce(operator.or_, q_objects)
            files = files.filter(query)

        # 分页
        page_number = request.GET.get('page')
        paginator = Paginator(files, 10)  # 每页显示 10 条记录
        page_obj = paginator.get_page(page_number)

        form = StoredFileForm()
        update_form = UpdateFileForm()

        return render(request, self.template_name, {'files': page_obj, 'form': form, 'update_form': update_form})

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if action == 'create':
            form = StoredFileForm(request.POST, request.FILES)
            if form.is_valid():
                stored_file = form.save(commit=False)
                stored_file.user = request.user
                stored_file.filename = request.FILES['file'].name
                stored_file.file_type = request.FILES['file'].content_type
                stored_file.size = request.FILES['file'].size
                stored_file.save()
                messages.success(request, '文件已成功创建！')
                return redirect('file-management')
            else:
                files = StoredFile.objects.filter(user=request.user, is_deleted=False)
                return render(request, self.template_name, {'files': files, 'form': form})
        elif action == 'update':
            file_id = request.POST.get('file_id')
            file = get_object_or_404(StoredFile, pk=file_id)
            form = UpdateFileForm(request.POST, request.FILES, instance=file)
            if form.is_valid():
                form.save()
                messages.success(request, '文件已成功更新！')
                return redirect('file-management')
            else:
                files = StoredFile.objects.filter(user=request.user, is_deleted=False)
                return render(request, self.template_name, {'files': files, 'form': form})
        elif action == 'delete':
            file_id = request.POST.get('file_id')
            file = get_object_or_404(StoredFile, pk=file_id)
            file.delete()
            messages.success(request, '文件已成功删除！')
            return redirect('file-management')
        else:
            messages.error(request, '无效的操作！')
            return redirect('file-management')
        


