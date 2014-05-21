# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BootstrapContainer'
        db.create_table(u'cmsplugin_bootstrap_grid_bootstrapcontainer', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('css_classes', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('fluid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cmsplugin_bootstrap_grid', ['BootstrapContainer'])

        # Adding model 'BootstrapRow'
        db.create_table(u'cmsplugin_bootstrap_grid_bootstraprow', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('css_classes', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_bootstrap_grid', ['BootstrapRow'])

        # Adding model 'BootstrapColumn'
        db.create_table(u'cmsplugin_bootstrap_grid_bootstrapcolumn', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('css_classes', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_bootstrap_grid', ['BootstrapColumn'])

        # Adding model 'ColumnAttribute'
        db.create_table(u'cmsplugin_bootstrap_grid_columnattribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bootstrap_column', self.gf('django.db.models.fields.related.ForeignKey')(related_name='column_attribute', to=orm['cmsplugin_bootstrap_grid.BootstrapColumn'])),
            ('attribute_type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('columns', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'cmsplugin_bootstrap_grid', ['ColumnAttribute'])


    def backwards(self, orm):
        # Deleting model 'BootstrapContainer'
        db.delete_table(u'cmsplugin_bootstrap_grid_bootstrapcontainer')

        # Deleting model 'BootstrapRow'
        db.delete_table(u'cmsplugin_bootstrap_grid_bootstraprow')

        # Deleting model 'BootstrapColumn'
        db.delete_table(u'cmsplugin_bootstrap_grid_bootstrapcolumn')

        # Deleting model 'ColumnAttribute'
        db.delete_table(u'cmsplugin_bootstrap_grid_columnattribute')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_bootstrap_grid.bootstrapcolumn': {
            'Meta': {'object_name': 'BootstrapColumn', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'css_classes': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'cmsplugin_bootstrap_grid.bootstrapcontainer': {
            'Meta': {'object_name': 'BootstrapContainer', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'css_classes': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'fluid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'cmsplugin_bootstrap_grid.bootstraprow': {
            'Meta': {'object_name': 'BootstrapRow', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'css_classes': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'cmsplugin_bootstrap_grid.columnattribute': {
            'Meta': {'object_name': 'ColumnAttribute'},
            'attribute_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'bootstrap_column': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'column_attribute'", 'to': u"orm['cmsplugin_bootstrap_grid.BootstrapColumn']"}),
            'columns': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['cmsplugin_bootstrap_grid']