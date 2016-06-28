# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'aula10/index.html', 
        {
            'nome': 'Allisson Azevedo',
            'namehtml' : '<b>Welton</b>'
        }
    )
