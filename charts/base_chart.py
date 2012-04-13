from random import randint

from django.core.exceptions import ImproperlyConfigured
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.http import HttpResponse

class BaseChart:
    slug = None
    display_name = None
    template = None
    
    width = None
    height = None

    def __init__(self, width=None, height=None, obj=None, obj_pk=None):
        if width:
            self.width = width
        if height:
            self.height = height
        if obj or obj_pk:
            self.object = obj or self.get_object(obj_pk)
        else:
            self.object = None

    def get_object(self, obj_pk):
        raise ImproperlyConfigured(_("Chart requires a definition of "
                                     "'get_object'"))

    def get_queryset(self):
        raise ImproperlyConfigured(_("Chart requires a definition of "
                                     "'get_queryset'"))

    def render(self, **context):
        context['chart'] = self
        context['div_id'] = randint(1,999999999)
        return render_to_string(self.template, context)

