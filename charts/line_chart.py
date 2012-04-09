from base_chart import BaseChart, ImproperlyConfigured, _

class LineChart(BaseChart):
    template = 'charts/render_line_chart.html'

    title = ''
    color = '#000000'
    line_color = '#FF0000'

    show_balloon = False
    use_dataset_colors = False
    value_text = '[[value]]'

    equal_spacing = True
    max_series = 5000

    class PeriodSelector:
        position = 'bottom'
        date_format = 'DD-MM-YYYY'
        input_fields_enabled = True
        from_text = 'From: '
        to_text = 'To: '
        periods_text = 'Periods: '
        periods = []
        # periods = [{'period': str,
        #             'label': str,
        #             'count': int,
        #             'selected': bool}, ...]
    
    def get_date(self, obj):
        raise ImproperlyConfigured(_("LineChart requires a definition of "
                                     "'get_date'"))

    def get_value(self, obj):
        raise ImproperlyConfigured(_("LineChart requires a definition of "
                                     "'get_value'"))
