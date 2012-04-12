from django.db.models import Model
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from charts import BaseChart

class ChartPool(object):
    def __init__(self):
        self._charts = {}
        self._models = []

    def register_chart(self, chart_class):
        if not issubclass(chart_class, BaseChart):
            raise ValueError(_('Registered class must be a subclass '
                               ' of charts.BaseChart)'))
        if not chart_class.slug:
            raise ImproperlyConfigured(_("Chart class must have a 'slug'"))
        self._charts[chart_class.slug] = chart_class

    def get_all_charts(self):
        return [(chart_slug, chart_class.display_name or chart_class.__name__)
                for chart_slug, chart_class in self._charts.items()]

    def get_chart_class(self, chart_slug):
        return self._charts.get(chart_slug)

    def register_model(self, model):
        if not issubclass(model, Model):
            raise ValueError(_('Registered model must be a subclass '
                               'of djando.db.models.Model'))
        content_type = ContentType.objects.get_for_model(model)
        self._models.append(content_type.id)

    def get_all_models(self):
        return self._models

chart_pool = ChartPool()
