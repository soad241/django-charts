from django import forms
from charts.cms_plugin.models import ChartPluginModel
from charts.cms_plugin import chart_pool


class ChartPluginModelForm(forms.ModelForm):
    chart_class = forms.ChoiceField()
    class Meta:
        fields = ('chart_class', 'title', 'width', 'height', 'content_type',
                  'object_id')
        model = ChartPluginModel

    def __init__(self, *args, **kwargs):
        super(ChartPluginModelForm, self).__init__(*args, **kwargs)
        self.fields['chart_class'].choices = chart_pool.get_choices()
        
