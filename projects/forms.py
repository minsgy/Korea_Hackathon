from django import forms
from .models import Project
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# CKeditor 위젯 폼 만들기
class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['description']

        widgets = {
            'description': forms.CharField(label=".", widget=CKEditorUploadingWidget()),
        }
