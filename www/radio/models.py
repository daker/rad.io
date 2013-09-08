# -*- coding: UTF-8 -*-
from django.db import models

from managers import *


class Category(models.Model):
    title = models.CharField("Title", max_length="255", blank=False, null=True)
    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)

class Network(models.Model):
    title = models.CharField("Title", max_length="255", blank=False, null=True)
    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)

class Continent(models.Model):
    title = models.CharField("Title", max_length="255", blank=False, null=True)
    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)

class Country(models.Model):
    title = models.CharField("Title", max_length="255", blank=False, null=True)
    continent = models.ForeignKey(Continent, verbose_name='Continent', related_name="continent_countries", blank=False, null=True)
    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)

class Language(models.Model):
    title = models.CharField("Title", max_length="255", blank=False, null=True)
    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)


class Station(models.Model):
    title = models.CharField("Title", max_length="255", blank=False, null=True)
    url = models.CharField("URL", max_length="255", blank=False, null=True)
    category = models.ForeignKey(Category, related_name='categories', null=True)
    network = models.ForeignKey(Network, related_name='networks', null=True)
    country = models.ForeignKey(Country, related_name='country', null=True)
    language = models.ForeignKey(Language, related_name='language', null=True)

    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)

class Source(models.Model):
    url = models.CharField("URL", max_length="255", blank=False, null=True)
    station = models.ForeignKey(Station, related_name='stations')

    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % (self.title)
