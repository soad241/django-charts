from django.core.exceptions import ImproperlyConfigured
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.http import HttpResponse

class BaseChart:
    width = 600
    height = 400
    template = None

    def get_queryset(self):
        raise ImproperlyConfigured(_("Chart requires a definition of "
                                     "'get_queryset'"))

    def render(self, **context):
        context['chart'] = self
        context['MEDIA_URL'] = settings.MEDIA_URL
        return render_to_string(self.template, context)
