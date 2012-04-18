from base_chart import BaseChart, ImproperlyConfigured, _

class Period(object):
    def __init__(self, period='', label='', count=None, selected=False):
        self.period = period
        self.label = label
        self.count = count
        self.selected = selected

class LineChart(BaseChart):
    template = 'charts/render_line_chart.html'

    title = ''
    show_category_axis = False
    percent_height = 70
    
    color = '#000000'
    line_color = '#FF0000'

    comparable = False
    show_balloon = False
    use_dataset_colors = False
    value_text = '[[value]]'

    equal_spacing = True
    max_series = 5000

    dataset_selector_position = 'left'

    class PeriodSelector:
        position = 'bottom'
        date_format = 'DD-MM-YYYY'
        input_fields_enabled = True
        from_text = 'From: '
        to_text = 'To: '
        periods_text = 'Periods: '
        periods = []
        # periods = [Period(period=str,
        #                   label=str,
        #                   count=int,
        #                   selected=bool), ...]
    
    def get_datasets(self):
        raise ImproperlyConfigured(_("Chart requires a definition of "
                                     "'get_datasets'"))
    
    def get_title(self, dataset):
        raise ImproperlyConfigured(_("LineChart requires a definition of "
                                     "'get_title'"))

    def get_color(self, dataset):
        raise ImproperlyConfigured(_("LineChart requires a definition of "
                                     "'get_color'"))

    def get_queryset(self, dataset):
        raise ImproperlyConfigured(_("Chart requires a definition of "
                                     "'get_queryset'"))

    def get_date(self, obj):
        raise ImproperlyConfigured(_("LineChart requires a definition of "
                                     "'get_date'"))

    def get_value(self, obj):
        raise ImproperlyConfigured(_("LineChart requires a definition of "
                                     "'get_value'"))
