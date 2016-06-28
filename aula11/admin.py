# -*- coding: utf-8 -*-
from django.contrib import admin

from aula11.models import Post, Category, UserInfo

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserInfo)