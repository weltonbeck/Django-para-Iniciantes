# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Tag(models.Model):

    name = models.CharField(
        u'Nome',
        max_length=50,
    )

    # generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        related_name='profile'
    )

    age = models.IntegerField(
        null=True,
    )

    twitter = models.URLField(
        u'Twitter',
        blank=True
    )

    tags = generic.GenericRelation(Tag)

    def __unicode__(self):
        return self.user.username




