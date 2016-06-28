# -*- coding: utf-8 -*-
from django import forms

from aula8.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'luke':
            raise forms.ValidationError(u'Esse nome é proibido!')
        return name
