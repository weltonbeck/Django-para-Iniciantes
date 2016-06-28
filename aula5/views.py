# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from aula5.models import Contato, Post, Categoria, Comentarios
from datetime import date

def index(request):

	# salvar
	# contato = Contato()
	# contato.nome = 'Teste'
	# contato.email = 'teste@teste.com'
	# contato.twitter = 'http://twitter.com/teste'
	# data = date(2004,2,9)
	# contato.data_nascimento = data
	# contato.save()
	# ----------------------

	# resgato 1 contato
	# contato = Contato.objects.get(id=1)
	# print contato
	# ----------------------

	# resgato uma lista filtrada do banco
	# contato = Contato.objects.filter(nome = 'teste')
	# print contato
	# ----------------------

	# resgato uma lista com todos
	# contato = Contato.objects.all()
	# print contato
	# ----------------------

	# salvo o post
	# post = Post(titulo='meu primeiro post', texto='texto do meu primeiro post')
	# post.save()
	# salvo as categorias do post
	# categoria1 = Categoria.objects.get(id=1)
	# categoria2 = Categoria.objects.get(id=2)
	# post.categoria.add(categoria1,categoria2)
	# ----------------------

	# salvo os comentarios
	# comentario = Comentarios(autor='josé manoel',comentarios='este é o comentario')
	# post = Post.objects.get(id = 1)
	# comentario.post = post
	# comentario.save()

	# pego os comentarios de um post
	# post = Post.objects.get(id = 1)
	# print post.comentarios.all()

	response = HttpResponse()
	response.write(u'contato')
	return response