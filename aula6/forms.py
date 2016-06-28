# -*- coding: utf-8 -*-
from django import forms

from aula6.models import Contact

# class ContactForm(forms.Form):
# 	first_name = forms.CharField(max_length=30,label='Nome')
# 	last_name = forms.CharField(max_length=30,label='Sobrenome')
# 	email = forms.EmailField(max_length=75,label='Email')
# 	twitter = forms.URLField(max_length=200,initial='Http://',label='Twitter')

# 	def save(self, contato = None):
# 		nome = self.cleaned_data.get('first_name')
# 		sobrenome = self.cleaned_data.get('last_name')
# 		email = self.cleaned_data.get('email')
# 		twitter = self.cleaned_data.get('twitter')
# 		if contato:
# 			contato.first_name = nome
# 			contato.last_name = sobrenome
# 			contato.email = email
# 			contato.twitter = twitter
# 			contato.save()
# 			return contato
# 		else:
# 			novo_contato = Contact(
# 				first_name=nome,
# 				last_name=sobrenome,
# 				email=email,
# 				twitter=twitter
# 			)
# 			novo_contato.save()
# 			return novo_contato

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		if Contact.objects.filter(email=email):
# 			raise forms.ValidationError(u"Email já cadastrado")

# 		return email

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		# fields = ('email','twitter')
		exclude = ('twitter')