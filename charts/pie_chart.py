import json

from base_chart import BaseChart, ImproperlyConfigured, _

class PieChart(BaseChart):
    template = 'charts/render_pie_chart.html'

    label_text = '[[percents]]%'
    label_radius = -35
    outline_color = '#FFFFF'
    outline_alpha = 0
    outline_thickness = 0
    
    has_legend = False

    class Legend:
        align = None
        marker_type = None
        position = None
        switchable = None

    def get_title(self, obj):
        raise ImproperlyConfigured(_("PieChart requires a definition of "
                                     "'get_title'"))

    def get_value(self, obj):
        raise ImproperlyConfigured(_("PieChart requires a definition of "
                                     "'get_value'"))

    def get_color(self, obj):
        return None

    def get_dataset_as_json(self):
        json_data = []
        for obj in self.get_queryset():
            json_data.append({'title': self.get_title(obj),
                              'value': self.get_value(obj) or 0.0,
                              'color': self.get_color(obj)})
        return json.dumps(json_data)

