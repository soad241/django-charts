from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from charts import BaseChart

class ChartPool(object):
    def __init__(self):
        self._charts = {}

    def register(self, chart_class):
        if not issubclass(chart_class, BaseChart):
            raise ValueError(_('Registered class must be a chart '
                             '(subclass of BaseChart)'))
        if not chart_class.slug:
            raise ImproperlyConfigured(_("Chart class must have a 'slug'"))
        self._charts[chart_class.slug] = chart_class

    def get_choices(self):
        return [(chart_slug, chart_class.display_name or chart_class.__name__)
                for chart_slug, chart_class in self._charts.items()]

    def get_chart_class(self, chart_slug):
        return self._charts.get(chart_slug)

chart_pool = ChartPool()
