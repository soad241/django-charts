from django import forms
from django.contrib.contenttypes.models import ContentType

from charts.cms_plugin.models import ChartPluginModel
from charts.cms_plugin import chart_pool

class ChartPluginModelForm(forms.ModelForm):
    chart_class = forms.ChoiceField()
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.none())

    class Meta:
        fields = ('chart_class', 'title', 'width', 'height', 'content_type',
                  'object_id')
        model = ChartPluginModel

    def __init__(self, *args, **kwargs):
        super(ChartPluginModelForm, self).__init__(*args, **kwargs)
        self.fields['chart_class'].choices = chart_pool.get_all_charts()
        self.fields['content_type'].queryset =\
                ContentType.objects.filter(id__in=chart_pool.get_all_models())
