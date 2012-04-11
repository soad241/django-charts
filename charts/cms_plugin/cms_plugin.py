from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from charts.cms_plugin.models import ChartPluginModel
from charts.cms_plugin import chart_pool

class ChartPlugin(CMSPluginBase):
    model = ChartPluginModel
    name = _("Chart Plugin")
    render_template = "charts/render_chart.html"

    def render(self, context, instance, placeholder):
        context['chart'] = chart_pool.get_chart_class(instance.chart_class)
        return context

plugin_pool.register_plugin(ChartPlugin)
