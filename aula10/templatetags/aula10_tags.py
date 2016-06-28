# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import User


register = template.Library()


@register.filter
@stringfilter
def swapcase(value):
    return value.swapcase()

@register.filter
@stringfilter
def bold(value):
    return '<b>%s</b>' % value

@register.filter
@stringfilter
def add_tag(value, arg):
    return '<%s>%s</%s>' % (arg, value, arg)


@register.assignment_tag
def get_user(username):
    try:
        user = User.objects.get(username=username)
    except:
        user = False
    return user


@register.inclusion_tag('aula10/show_users.html')
def show_users():
    users = User.objects.all()
    return {'users': users}