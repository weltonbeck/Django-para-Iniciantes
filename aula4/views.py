# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	# from django import template
	# t = template.Template('menu nome é {{ nome|upper }}.')
	# c = template.Context({'nome': 'Teste'})
	# print t.render(c) # printa no terminarl
	# --------------------------

	# template_string = '''
	# 	{% if idade >= 20 %}
	# 	A idade é maior ou igual a 20
	# 	{% else %}
	# 	A idade é menor que 20
	# 	{% endif %}
	# 	'''
	# t = template.Template(template_string)
	# c = template.Context({'idade': 19})
	# print t.render(c) # printa no terminarl
	# --------------------------
	lista = [
		u'joão',
		u'josé',
		u'lek'
	]
	return render(request, 'aula4/index.html', {'nome' : 'Teste', 'idade' : 19, 'lista' : lista})