# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from aula6.models import Contact
from aula6.forms import ContactForm

def index(request):
	contatos = Contact.objects.all()

	# if request.method == 'POST':
	# 	nome = request.POST.get('first_name')
	# 	sobrenome = request.POST.get('last_name')
	# 	email = request.POST.get('email')
	# 	twitter = request.POST.get('twitter')

	# 	novo_contato = Contact(
	# 		first_name=nome,
	# 		last_name=sobrenome,
	# 		email=email,
	# 		twitter=twitter
	# 	)
	# 	novo_contato.save()
	# 	HttpResponseRedirect(reverse('aula6_index'))
	# else:
	# 	nome = ''
	# 	sobrenome = ''
	# 	email = ''
	# 	twitter = ''

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid() :
			novo_contato = form.save()

			HttpResponseRedirect(reverse('aula6_index'))
	else:
		form = ContactForm()

	return render(request, 'aula6/index.html', {
			'contatos': contatos,
			'form' : form
		}
	)

def detail(request, id):
	contatos = Contact.objects.all()

	contato = get_object_or_404(Contact, id=id)
	if request.method == 'POST':
		# form = ContactForm(request.POST)
		form = ContactForm(request.POST,instance=contato)
		if form.is_valid() :
			# novo_contato = form.save(contato=contato)
			novo_contato = form.save()

			HttpResponseRedirect(reverse('aula6_index'))
	else:
		# initial = {
		# 	'first_name' : contato.first_name,
		# 	'last_name' : contato.last_name,
		# 	'email' : contato.email,
		# 	'twitter' : contato.twitter,
		# }
		# form = ContactForm(initial = initial)
		form = ContactForm(instance=contato)
	return render(request, 'aula6/index.html', {
			'contatos': contatos,
			'form' : form
		}
	)
