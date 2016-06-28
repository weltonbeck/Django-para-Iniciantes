# -*- coding: utf-8 -*-
from django import forms

from aula13.models import UploadFile


class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = UploadFile