from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class compHtml(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    extrastyle = models.TextField(null=True,blank=True)
    extrascript = models.TextField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    