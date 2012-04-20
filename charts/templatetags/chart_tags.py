from django import template

register = template.Library()

@register.simple_tag
def xy_chart_get_label_text(chart, obj):
    return chart.get_label_text(obj)

@register.simple_tag
def xy_chart_get_color(chart, obj, selected=False):
    return chart.get_color(obj, selected)

@register.simple_tag
def xy_chart_get_text_color(chart, obj, selected=False):
    return chart.get_text_color(obj, selected)

@register.simple_tag
def line_chart_get_title(chart, dataset):
    return chart.get_title(dataset)

@register.simple_tag
def line_chart_get_color(chart, dataset):
    return chart.get_color(dataset)
