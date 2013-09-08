# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Category, Station, Source, Network, Language, Continent, Country

import json


def categories(request):
    categories_json = {'objects': []}
    cats = Category.objects.all()
    for c in cats:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        categories_json['objects'].append(infos)

    return HttpResponse(json.dumps(categories_json), content_type="application/json")


def category(request, id):
    stations_json = {'objects': []}

    stations = Station.objects.filter(category__pk=id)

    for s in stations:
        sources = Source.objects.filter(station__pk=s.id)[:1]
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    return HttpResponse(json.dumps(stations_json), content_type="application/json")


def continent(request):
    continents_json = {'objects': []}
    cats = Continent.objects.all()
    for c in cats:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        continents_json['objects'].append(infos)
    return HttpResponse(json.dumps(continents_json), content_type="application/json")


def country(request, id):
    country_json = {'objects': []}

    countries = Country.objects.filter(continent__pk=id)
    for c in countries:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        country_json['objects'].append(infos)

    return HttpResponse(json.dumps(country_json), content_type="application/json")


def countrystations(request, id):
    countrystations_json = {'objects': []}

    countriesstations = Station.objects.filter(country__pk=id)
    for s in countriesstations:
        sources = Source.objects.filter(station__pk=s.id)[:1]
        infos = {
            'id': s.id,
            'title': s.title,
            'source': sources[0].url
        }
        countrystations_json['objects'].append(infos)

    return HttpResponse(json.dumps(countrystations_json), content_type="application/json")


def languages(request):

    languages_json = {'objects': []}
    lngs = Language.objects.all()
    for c in lngs:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        languages_json['objects'].append(infos)

    return HttpResponse(json.dumps(languages_json), content_type="application/json")


def language(request, id):
    stations_json = {'objects': []}

    stations = Station.objects.filter(language__pk=id)
    for s in stations:
        sources = Source.objects.filter(station__pk=s.id)[:1]
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    return HttpResponse(json.dumps(stations_json), content_type="application/json")


def networks(request):

    networks_json = {'objects': []}
    networks = Network.objects.all()
    for c in networks:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        networks_json['objects'].append(infos)

    return HttpResponse(json.dumps(networks_json), content_type="application/json")


def network(request, id):
    stations_json = {'objects': []}

    stations = Station.objects.filter(network__id=id)

    for s in stations:
        sources = Source.objects.filter(station__id=s.id)[:1]
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    return HttpResponse(json.dumps(stations_json), content_type="application/json")


def station(request, id):
    station_json = {'objects': []}
    s = get_object_or_404(Station, id=id)
    sources = Source.objects.filter(station__id=s.id)[:1]
    infos = {
        'id': s.id,
        'title': s.title,
        'url': s.url,
        'source': sources[0].url
    }
    station_json['objects'].append(infos)

    return HttpResponse(json.dumps(station_json), content_type="application/json")



def search(request):
    q = request.GET.get('q')
    stations_json = {'objects': []}
    stations = Station.objects.filter(title__contains=q)
    for s in stations:
        sources = Source.objects.filter(station__id=s.id)[:1]
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    return HttpResponse(json.dumps(stations_json), content_type="application/json")


def nearby(request):
    q = request.GET.get('q')
    stations_json = {'objects': []}
    stations = Station.objects.filter(country__title=q)
    for s in stations:
        sources = Source.objects.filter(station__pk=s.id)[:1]
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    return HttpResponse(json.dumps(stations_json), content_type="application/json")
