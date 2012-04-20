from base_chart import BaseChart, ImproperlyConfigured, _

class XYChart(BaseChart):
    template = 'charts/render_xy_chart.html'

    line_alpha = 0
    start_duration = 0
    font_family = 'Arial'
    
    bullet_text = '([[x]], [[y]])'
    bullet_shape = 'round'
    bullet_size = 20

    selected_bullet_shape = 'round'
    selected_bullet_size = 40

    class XAxis:
        title = None
        position = 'bottom'
        auto_grid_count = True

    class YAxis:
        title = None
        position = 'left'
        auto_grid_count = True

    def get_selected(self):
        return None

    def get_label_text(self, obj):
        raise ImproperlyConfigured(_("XYChart requires a definition of "
                                     "'get_label_text'"))

    def get_xy_values(self, obj):
        raise ImproperlyConfigured(_("XYChart requires a definition of "
                                     "'get_xy_values'"))

    def get_color(self, obj, selected=False):
        raise ImproperlyConfigured(_("XYChart requires a definition of "
                                     "'get_color'"))

    def get_text_color(self, obj, selected=False):
        raise ImproperlyConfigured(_("XYChart requires a definition of "
                                     "'get_text_color'"))        

    def get_dataset_as_json(self):
        json_data = []
        idx = 1
        for obj in self.get_queryset():
            x, y = self.get_xy_values(obj)
            json_data.append({'x%i' % idx: x or 0.0,
                              'y%i' % idx: y or 0.0})
            idx += 1
        return json.dumps(json_data)

