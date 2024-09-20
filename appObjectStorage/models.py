

from typing import Any
from django.db import models
from django.contrib.auth.models import User

class StoredFile(models.Model):
    id = models.AutoField(primary_key=True)
    
    # 文件对象
    file = models.FileField(upload_to='objectsstorage/BaiduSyncdisk/objstorage')
    
    # 文件名
    filename = models.CharField(max_length=255)
    
    # 文件大小
    size = models.BigIntegerField()
    
    # 文件类型
    file_type = models.CharField(max_length=50, blank=True, null=True)
    
    # 存储桶（bucket）
    bucket = models.CharField(max_length=100, blank=True, null=True)
    
    # 文件描述
    description = models.TextField(blank=True, null=True)
    
    # 标签
    tags = models.CharField(max_length=255, blank=True, null=True)

    # 上传时间
    upload_time = models.DateTimeField(auto_now_add=True)
    
    # 最后修改时间
    last_modified = models.DateTimeField(auto_now=True)
    
    # 用户信息
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 是否删除
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.filename
    
    @property
    def get_absolute_url(self):
        """
        获取文件的绝对URL。

        返回:
            str -- 文件的绝对URL。
        """
        return '/media/' + str(self.file)
    
    #重新删除记录逻辑，记录删除时，将记录is_delete设置为True
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
        return