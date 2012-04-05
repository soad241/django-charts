from django.shortcuts import render_to_response
from django.template import RequestContext

def generate_chart_view(request, chart_class, obj_pk=None, **context):
    context['chart'] = chart_class(obj_pk)
    return render_to_response('charts/render_chart.html', context,
                              context_instance=RequestContext(request))
