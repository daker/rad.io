# -*- coding: UTF-8 -*-

from django.db import models


class ArtisteManager(models.Manager):

    def published(self):
        return self.filter(is_public=True).order_by('-pk')


class TrackManager(models.Manager):

    def published(self):
        return self.filter(is_public=True).order_by('-pk')
