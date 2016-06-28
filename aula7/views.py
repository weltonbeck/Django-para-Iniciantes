# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from aula7.forms import LoginForm

# from django.contrib.auth.models import User
# from aula7.models import UserProfile

def index(request):

	# crio um profile vazio para um usuario
	# usuario = User.objects.get(id=1)
	# profile = UserProfile.objects.create(user=usuario)
	# print profile
	# print usuario.user_profile
	# print usuario.get_profile() -- funciona se definir variavel no settings AUTH_PROFILE_MODULE
	# ----------------------------
	next = request.REQUEST.get('next', '/aula7/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			# logo o usuario
			login(request, user)
			return HttpResponseRedirect(next)
	else:
		form = LoginForm()
	return render(request, 'aula7/index.html', 
		{
			'form': form,
			'next': next,
		}
	)


def sair(request):
	logout(request)
	return HttpResponseRedirect(reverse('aula7_index'))


@login_required
def view_protegida(request):
	return HttpResponse('View protegida!')


@permission_required('aula5.add_categoria')
def view_protegida2(request):
	return HttpResponse('View protegida2!')