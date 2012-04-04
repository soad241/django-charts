from base_chart import BaseChart, ImproperlyConfigured, _

class XYChart(BaseChart):
    template = 'charts/render_xy_chart.html'

    line_alpha = 0
    start_duration = 0
    font_family = 'Arial'
    
    bullet_text = "([[x]], [[y]])"
    bullet_shape = 'round'
    bullet_size = 20
    bullet_color = '#595959'
    bullet_text_color = '#595959'

    selected_bullet_shape = 'round'
    selected_bullet_size = 40
    selected_bullet_color = '#A042C2'
    selected_bullet_text_color = '#000000'

    class XAxis:
        title = None
        position = 'bottom'
        auto_grid_count = True

    class YAxis:
        title = None
        position = 'left'
        auto_grid_count = True

    def get_label_text(self, obj):
        raise ImproperlyConfigured(_("XYChart requires a definition of "
                                     "'get_label_text'"))

    def get_xy_values(self, obj):
        raise ImproperlyConfigured(_("XYChart requires a definition of "
                                     "'get_xy_values'"))

    def get_selected(self):
        return None

