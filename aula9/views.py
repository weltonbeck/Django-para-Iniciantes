# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout

from aula7.forms import LoginForm


def index(request): 
    next = request.REQUEST.get('next', '/aula7/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(next)
    else:
        form = LoginForm()
    return render(request, 'aula9/index.html', 
        {
            'form': form,
            'next': next,
        }
    )
    #return render(request, 'aula9/index.html')