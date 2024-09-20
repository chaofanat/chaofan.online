from django import forms
from .models import StoredFile

class StoredFileForm(forms.ModelForm):
    class Meta:
        model = StoredFile
        fields = ['file','bucket', 'description', 'tags']


    def clean_file(self):
        file = self.cleaned_data.get('file')
        max_size = 10 * 1024 * 1024  # 10 MB

        if file and file.size > max_size:
            raise forms.ValidationError("文件大小不能超过 10 MB。")
        return file
    

class UpdateFileForm(forms.ModelForm):
    class Meta:
        model = StoredFile
        fields = ['description', 'tags', 'bucket']