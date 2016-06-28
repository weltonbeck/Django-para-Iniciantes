# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from aula13.forms import UploadFileForm


def index(request):
    if request.session.get('view_this_page', False):
        visitou = True
    else:
        visitou = False
        request.session['view_this_page'] = True
    return render(request, 'aula13/index.html',
        {'visitou': visitou}
    )