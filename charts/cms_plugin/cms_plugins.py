from django.utils.translation import ugettext as _

from settings import MEDIA_URL
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from charts.cms_plugin.models import ChartPluginModel
from charts.cms_plugin.forms import ChartPluginModelForm
from charts.cms_plugin import chart_pool

class ChartPlugin(CMSPluginBase):
    model = ChartPluginModel
    name = _("Chart")
    form = ChartPluginModelForm
    render_template = "charts/render_chart.html"

    def render(self, context, instance, placeholder):
        chart_class = chart_pool.get_chart_class(instance.chart_class)
        context['chart'] = chart_class(width=instance.width,
                                       height=instance.height,
                                       obj=instance.content_object)
        return context

    class Media:
        js = (MEDIA_URL + 'charts/amstocks/amstock.js',
              MEDIA_URL + 'charts/amstocks/raphael.js')
        css = (MEDIA_URL + 'charts/amstocks/style.css',)

plugin_pool.register_plugin(ChartPlugin)
