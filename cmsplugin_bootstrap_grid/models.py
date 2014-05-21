# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class BootstrapContainer(CMSPlugin):
    css_classes = models.CharField(max_length=128, blank=True, null=True, 
        help_text=u"Enter a comma delimited list of classes")
    fluid = models.BooleanField(default=False)
    
    def __str__(self):
        return u"BootstrapContainer_%s" % self.cmsplugin_ptr_id

    def __unicode__(self):
        return u"%s" % self.get_css_classes()

    def get_css_classes(self):
        classes = u"container"
        if self.fluid:
            classes += u"-fluid"
        classes = u"%s %s" % (classes, self.css_classes.replace(",", " "))
        return classes


class BootstrapRow(CMSPlugin):
    css_classes = models.CharField(max_length=128, blank=True, null=True, 
        help_text="Enter a comma delimited list of classes")

    def __str__(self):
        return u"BootstrapRow_%s" % self.cmsplugin_ptr_id

    def __unicode__(self):
        return u"%s" % self.get_css_classes()

    def get_css_classes(self):
        return u"%s %s" % ("row", self.css_classes.replace(",", " "))


class BootstrapColumn(CMSPlugin):
    css_classes = models.CharField(max_length=128, blank=True, null=True, 
        help_text=u"Enter a comma delimited list of classes")

    def __str__(self):
        return u"BootstrapColumn_%s" % self.cmsplugin_ptr_id

    def __unicode__(self):
        return u"%s" % self.get_css_classes()

    def copy_relations(self, oldinstance):
        for item in oldinstance.columnattribute_set.all():
            item.pk = None
            item.bootstrap_column = self
            item.save()

    def get_css_classes(self):
        classes = u" ".join([attribute.get_css_class() for attribute in self.column_attribute.all()])
        classes = u"%s %s" % (classes, self.css_classes.replace(",", " "))
        return classes

class ColumnAttribute(models.Model):

    bootstrap_column = models.ForeignKey(BootstrapColumn, 
        related_name='column_attribute')

    attribute_type = models.CharField(max_length=64, choices=(
        ('column', 'Column'),
        ('offset', 'Offset'),
        ('pull', 'Pull'),
        ('push', 'Push'),
        ('hidden', 'Hidden at Column Size'),
        ('visible', 'Visible at Column Size')
    ))

    size = models.CharField(max_length=64, choices=(
        ('xs', 'Extra small devices (<768px)'),
        ('sm', 'Small devices (>767px)'),
        ('md', 'Medium devices (>991px)'),
        ('lg', 'Large devices (>1199px)'),
    ))
    columns = models.IntegerField(choices=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
    ))

    def __str__(self):
        return u"ColumnAttribute_%s" % self.id

    def __unicode__(self):
        return u"%s" % self.get_css_class()

    def get_css_class(self):
        if self.attribute_type in ('hidden', 'visible'):
            return u"%s-%s" % (self.attribute_type, self.size)
        elif self.attribute_type == 'column':
            return u"col-%s-%s" % (self.size, self.columns)
        else:
            return u"col-%s-%s-%s" % (self.size, self.attribute_type, self.columns)

