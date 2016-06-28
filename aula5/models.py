# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Contato(models.Model):
	
	nome = models.CharField(max_length=255)
	email = models.EmailField()
	twitter = models.URLField()
	data_nascimento = models.DateField()

	def __unicode__(self):
		return self.nome

class Categoria(models.Model):

	nome = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome

class Post(models.Model):

	titulo = models.CharField(max_length=200)
	texto = models.TextField(max_length=1024)
	categoria = models.ManyToManyField(Categoria)

	def __unicode__(self):
		return self.titulo

class Comentarios(models.Model):

	autor = models.CharField(max_length=100)
	comentarios = models.TextField(max_length=1024)
	post = models.ForeignKey(Post,related_name='comentarios')

	def __unicode__(self):
		return self.autor