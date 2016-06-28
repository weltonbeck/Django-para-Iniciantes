# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TestIndexView(TestCase):

    def setUp(self):
        self.url = reverse('aula9_index')
        self.user1 = User.objects.create_user('user1', 'user1@email.com', '123456')

    def test_render(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, u'Faça seu login')

    def test_form_empty(self):
        response = self.client.post(self.url)
        self.assertFormError(
            response, 
            'form', 
            'username', 
            u'Este campo é obrigatório.'
        )
        self.assertFormError(
            response, 
            'form', 
            'password', 
            u'Este campo é obrigatório.'
        )

    def test_form_with_invalid_username(self):
        response = self.client.post(
            self.url, 
            {
                'username': u'fulano',
            }
        )
        self.assertFormError(
            response, 
            'form', 
            'username', 
            u'Esse nome de usuário não existe.'
        )

    def test_form_with_invalid_password(self):
        response = self.client.post(
            self.url, 
            {
                'username': u'user1',
                'password': u'1234567'
            }
        )
        self.assertFormError(
            response, 
            'form', 
            'password', 
            u'Senha incorreta.'
        )

    def test_form_ok(self):
        response = self.client.post(
            self.url, 
            {
                'username': u'user1',
                'password': u'123456'
            }
        )
        self.assertRedirects(response, reverse('aula7_index'))
