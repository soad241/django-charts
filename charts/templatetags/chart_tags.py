from django import template

register = template.Library()

@register.filter
def jsfloatformat(value):
    try:
        return str(float(value)).replace(',', '.')
    except ValueError:
        return value

@register.inclusion_tag('charts/pie_chart_obj_info.html')
def pie_chart_obj_info(chart, obj):
    return {'title': chart.get_title(obj),
            'value': chart.get_value(obj),
            'color': chart.get_color(obj)}

@register.inclusion_tag('charts/xy_chart_obj_info.html')
def xy_chart_obj_info(chart, obj, div_id, idx):
    x, y = chart.get_xy_values(obj)
    return {'x': x,
            'y': y,
            'div_id': div_id,
            'idx': idx}

@register.inclusion_tag('charts/xy_chart_bullet_info.html')
def xy_chart_bullet_info(chart, obj, div_id, idx, selected=False):
    return {'chart': chart,
            'label_text': chart.get_label_text(obj),
            'color': chart.get_color(obj, selected),
            'text_color': chart.get_text_color(obj, selected),
            'div_id': div_id,
            'idx': idx,
            'selected': selected}

@register.inclusion_tag('charts/line_chart_obj_info.html')
def line_chart_obj_info(chart, obj):
    return {'date': chart.get_date(obj),
            'value': chart.get_value(obj)}
