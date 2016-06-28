# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	# response = HttpResponse()
	# response.write(u'Olá Mundo!')
	# return response
	# -----------------------------

	# return HttpResponse(u'Olá Mundo!', content_type='text/plain')
	# return HttpResponseRedirect('http://www.google.com.br')
	# -----------------------------

	# nome = request.GET.get('nome', u'não tem nome') # caso n tenha ele joga o segundo
	# # nome = request.GET['nome']
	# return HttpResponse(u'O nome é %s' % nome)
	# -----------------------------

	# lista = request.GET.items()
	# return HttpResponse(lista)
	# -----------------------------

	if request.method == 'POST':
		name = request.POST.get('name', 'sem nome')
		return HttpResponse(u'O nome é %s' % name)
	else:
		formulario = '''
		<form action="." method="post">
			<input type="text" name="name" maxlength="100" />
			<button type="submit">Enviar</button>
		</form>
		'''
		return HttpResponse(formulario)

def detail(request, id ):
	return HttpResponse(u'O id é: %s' % id)


