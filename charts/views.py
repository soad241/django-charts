from django.shortcuts import render_to_response
from django.template import RequestContext

def generate_chart_view(request, chart_class, **context):
    context['chart'] = chart_class()
    return render_to_response('charts/render_chart.html', context,
                              context_instance=RequestContext(request))
