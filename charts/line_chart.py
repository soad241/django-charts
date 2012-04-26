from base_chart import BaseChart, ImproperlyConfigured, _

def serialize_datetime(dt):
    """ Serialize date, datetime and anything that behaves like them """
    pattern =\
        'new Date({year},{month},{day},{hour},{minute},{second},{microsecond})'
    return pattern.format(year=getattr(dt, 'year', 1990),
                          month=getattr(dt, 'month', 1)-1,
                          day=getattr(dt, 'day', 1),
                          hour=getattr(dt, 'hour', 0),
                          minute=getattr(dt, 'minute', 0),
                          second=getattr(dt, 'second', 0),
                          microsecond=getattr(dt, 'microsecond', 0))

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
    comparable = True
    show_balloon = False
    use_dataset_colors = False
    value_text = '[[value]]'

    equal_spacing = True
    max_series = 5000

    has_data_selector = False
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
    
    def get_dataset_as_json(self):
        json_data = []
        for dataset in self.get_datasets():
            dataset_data = []
            for obj in self.get_queryset(dataset):
                date = serialize_datetime(self.get_date(obj))
                value = self.get_value(obj) or 0.0
                dataset_data.append('{"date": %s, "value": %s}' % (date, value))
            json_data.append('[%s]' % ', '.join(dataset_data))
        return json_data

