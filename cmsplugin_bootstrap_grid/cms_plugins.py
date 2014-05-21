# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import BootstrapContainer, BootstrapRow, BootstrapColumn, ColumnAttribute

class BootstrapContainerPlugin(CMSPluginBase):

    model = BootstrapContainer
    name = _("Bootstrap Container")
    module = "Bootstrap Grid"
    render_template = "cmsplugin_bootstrap_grid/container.html"
    allow_children = True
    child_classes = ['BootstrapRowPlugin']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

class BootstrapRowPlugin(CMSPluginBase):

    model = BootstrapRow
    name = _("Bootstrap Row")
    module = "Bootstrap Grid"
    render_template = "cmsplugin_bootstrap_grid/row.html"
    allow_children = True
    child_classes = ['BootstrapColumnPlugin']
    parent_classes = ['BootstrapContainerPlugin', 'BootstrapColumnPlugin']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

class ColumnAttributeInline(admin.TabularInline):
    model = ColumnAttribute
    extra = 1

class BootstrapColumnPlugin(CMSPluginBase):

    model = BootstrapColumn
    name = _("Bootstrap Column")
    module = "Bootstrap Grid"
    render_template = "cmsplugin_bootstrap_grid/column.html"
    allow_children = True

    inlines = [ColumnAttributeInline]


    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(BootstrapContainerPlugin)
plugin_pool.register_plugin(BootstrapRowPlugin)
plugin_pool.register_plugin(BootstrapColumnPlugin)
