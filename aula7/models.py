# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        related_name='user_profile'
    )

    birthday = models.DateField(
        u'Aniversário',
        null=True
    )

    def __unicode__(self):
        return self.user.username
