# coding:utf-8
from django import forms
from .models import SharedFile

class UploadForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['name', 'file']