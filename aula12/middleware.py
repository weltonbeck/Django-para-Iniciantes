# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

class LoginRequiredMiddleware(object):

    def process_request(self, request):
        LOGIN_URL = settings.LOGIN_URL
        if not request.user.is_authenticated() and request.path != LOGIN_URL:
            return HttpResponseRedirect(LOGIN_URL)
