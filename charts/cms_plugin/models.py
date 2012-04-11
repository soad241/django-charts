from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from cms.models import CMSPlugin
from charts.cms_plugin import chart_pool

class ChartPluginModel(CMSPlugin):
    chart_class = models.CharField(max_length=64,
                                   choices=chart_pool.get_choices())
    title = models.CharField(max_length=256, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
      return self.title
