# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'aula12/index.html', 
    )
