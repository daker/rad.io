from flask import Flask
from flask import Response
from flask import json
from flask import request
from peewee import *
from flask_peewee.db import Database

try:
    import simplejson as json
except ImportError:
    import json

# configure our database
DATABASE = {
    'name': 'peewee.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

class Category(db.Model):
    title = CharField()

class Network(db.Model):
    title = CharField()

class Continent(db.Model):
    title = CharField()

class Country(db.Model):
    title = CharField()
    continent = ForeignKeyField(Continent, related_name='continent')

class Language(db.Model):
    title = CharField()


class Station(db.Model):
    title = CharField()
    url = CharField()
    category = ForeignKeyField(Category, related_name='categories', null=True)
    network = ForeignKeyField(Network, related_name='networks', null=True)
    country = ForeignKeyField(Country, related_name='country', null=True)
    language = ForeignKeyField(Language, related_name='language', null=True)


class Source(db.Model):
    url = CharField()
    station = ForeignKeyField(Station, related_name='stations')

@app.route('/api/category/')
def categories():

    categories_json = {'objects': []}
    cats = Category.select()
    for c in cats:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        categories_json['objects'].append(infos)
    resp = Response(json.dumps(categories_json), status=200, mimetype='application/json')
    return resp

@app.route('/api/category/<int:id>/')
def category(id):
    stations_json = {'objects': []}

    stations = Station.select().join(Category).where(Category.id == id)

    for s in stations:
        sources = Source.select().join(Station).where(Station.id == s.id).limit(1)
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    resp = Response(json.dumps(stations_json), status=200, mimetype='application/json')
    return resp


@app.route('/api/continent/')
def continent():
    continents_json = {'objects': []}
    cats = Continent.select()
    for c in cats:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        continents_json['objects'].append(infos)
    resp = Response(json.dumps(continents_json), status=200, mimetype='application/json')
    return resp

@app.route('/api/continent/<int:id>/')
def country(id):
    country_json = {'objects': []}

    countries = Country.select().join(Continent).where(Continent.id == id)
    for c in countries:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        country_json['objects'].append(infos)

    resp = Response(json.dumps(country_json), status=200, mimetype='application/json')
    return resp


@app.route('/api/country/<int:id>/')
def countrystations(id):
    countrystations_json = {'objects': []}

    countriesstations = Station.select().join(Country).where(Country.id == id)
    for s in countriesstations:
        sources = Source.select().join(Station).where(Station.id == s.id).limit(1)
        infos = {
            'id': s.id,
            'title': s.title,
            'source': sources[0].url
        }
        countrystations_json['objects'].append(infos)

    resp = Response(json.dumps(countrystations_json), status=200, mimetype='application/json')
    return resp

@app.route('/api/language/')
def languages():

    languages_json = {'objects': []}
    lngs = Language.select()
    for c in lngs:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        languages_json['objects'].append(infos)
    resp = Response(json.dumps(languages_json), status=200, mimetype='application/json')
    return resp

@app.route('/api/language/<int:id>/')
def language(id):
    stations_json = {'objects': []}

    stations = Station.select().join(Language).where(Language.id == id)

    for s in stations:
        sources = Source.select().join(Station).where(Station.id == s.id).limit(1)
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    resp = Response(json.dumps(stations_json), status=200, mimetype='application/json')
    return resp


@app.route('/api/network/')
def networks():

    networks_json = {'objects': []}
    networks = Network.select()
    for c in networks:
        infos = {
            'id': c.id,
            'title': c.title,
        }
        networks_json['objects'].append(infos)
    resp = Response(json.dumps(networks_json), status=200, mimetype='application/json')
    return resp

@app.route('/api/network/<int:id>/')
def network(id):
    stations_json = {'objects': []}

    stations = Station.select().join(Network).where(Network.id == id)

    for s in stations:
        sources = Source.select().join(Station).where(Station.id == s.id).limit(1)
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)

    resp = Response(json.dumps(stations_json), status=200, mimetype='application/json')
    return resp


@app.route('/api/station/<int:id>/')
def station(id):
    station_json = {'objects': []}
    s = Station.get(Station.id == id)
    sources = Source.select().join(Station).where(Station.id == s.id)
    infos = {
        'id': s.id,
        'title': s.title,
        'url': s.url,
        'source': sources[0].url
    }
    station_json['objects'].append(infos)
    resp = Response(json.dumps(station_json), status=200, mimetype='application/json')
    return resp

@app.route('/api/search/', methods=["GET"])
def search():
    q = request.args['q']
    q = "*%s*" % q
    stations_json = {'objects': []}
    stations = Station.select().where(Station.title % q)
    for s in stations:
        sources = Source.select().join(Station).where(Station.id == s.id).limit(1)
        infos = {
            'id': s.id,
            'title': s.title,
            'url': s.url,
            'source': sources[0].url
        }
        stations_json['objects'].append(infos)
    resp = Response(json.dumps(stations_json), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    import os
    Category.create_table(fail_silently=True)
    Continent.create_table(fail_silently=True)
    Country.create_table(fail_silently=True)
    Network.create_table(fail_silently=True)
    Language.create_table(fail_silently=True)
    Station.create_table(fail_silently=True)
    Source.create_table(fail_silently=True)


    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)