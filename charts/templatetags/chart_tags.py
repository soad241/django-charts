from django import template

register = template.Library()

@register.filter
def jsfloatformat(value):
    try:
        return str(float(jsfloatformat)).replace(',', '.')
    except ValueError:
        return value

@register.inclusion_tag('charts/pie_chart_obj_info.html')
def pie_chart_obj_info(chart, obj):
    return {'title': chart.get_title(obj),
            'value': chart.get_value(obj),
            'color': chart.get_color(obj)}

@register.inclusion_tag('charts/xy_chart_obj_info.html')
def xy_chart_obj_info(chart, obj, idx):
    x, y = chart.get_xy_values(obj)
    return {'x': x,
            'y': y,
            'idx': idx}
