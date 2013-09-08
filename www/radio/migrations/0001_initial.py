# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('radio_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
        ))
        db.send_create_signal('radio', ['Category'])

        # Adding model 'Network'
        db.create_table('radio_network', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
        ))
        db.send_create_signal('radio', ['Network'])

        # Adding model 'Continent'
        db.create_table('radio_continent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
        ))
        db.send_create_signal('radio', ['Continent'])

        # Adding model 'Country'
        db.create_table('radio_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
            ('continent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='continent_countries', null=True, to=orm['radio.Continent'])),
        ))
        db.send_create_signal('radio', ['Country'])

        # Adding model 'Language'
        db.create_table('radio_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
        ))
        db.send_create_signal('radio', ['Language'])

        # Adding model 'Station'
        db.create_table('radio_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='categories', null=True, to=orm['radio.Category'])),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(related_name='networks', null=True, to=orm['radio.Network'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='country', null=True, to=orm['radio.Country'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='language', null=True, to=orm['radio.Language'])),
        ))
        db.send_create_signal('radio', ['Station'])

        # Adding model 'Source'
        db.create_table('radio_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length='255', null=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stations', to=orm['radio.Station'])),
        ))
        db.send_create_signal('radio', ['Source'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('radio_category')

        # Deleting model 'Network'
        db.delete_table('radio_network')

        # Deleting model 'Continent'
        db.delete_table('radio_continent')

        # Deleting model 'Country'
        db.delete_table('radio_country')

        # Deleting model 'Language'
        db.delete_table('radio_language')

        # Deleting model 'Station'
        db.delete_table('radio_station')

        # Deleting model 'Source'
        db.delete_table('radio_source')


    models = {
        'radio.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        },
        'radio.continent': {
            'Meta': {'object_name': 'Continent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        },
        'radio.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'continent_countries'", 'null': 'True', 'to': "orm['radio.Continent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        },
        'radio.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        },
        'radio.network': {
            'Meta': {'object_name': 'Network'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        },
        'radio.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'to': "orm['radio.Station']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        },
        'radio.station': {
            'Meta': {'object_name': 'Station'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'null': 'True', 'to': "orm['radio.Category']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country'", 'null': 'True', 'to': "orm['radio.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'language'", 'null': 'True', 'to': "orm['radio.Language']"}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'networks'", 'null': 'True', 'to': "orm['radio.Network']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True'})
        }
    }

    complete_apps = ['radio']