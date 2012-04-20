from django import template

register = template.Library()

@register.filter
def jsfloatformat(value):
    try:
        return str(float(value)).replace(',', '.')
    except ValueError:
        return value

@register.inclusion_tag('charts/xy_chart_obj_info.html')
def xy_chart_obj_info(chart, obj, selected=False):
    return {'label_text': chart.get_label_text(obj),
            'color': chart.get_color(obj, selected),
            'text_color': chart.get_text_color(obj, selected)}

@register.inclusion_tag('charts/line_chart_dataset_info.html')
def line_chart_dataset_info(chart, dataset):
    return {'chart': chart,
            'queryset': chart.get_queryset(dataset)}

@register.inclusion_tag('charts/line_chart_obj_info.html')
def line_chart_obj_info(chart, obj):
    return {'date': chart.get_date(obj),
            'value': chart.get_value(obj)}

@register.inclusion_tag('charts/line_chart_dataset_detail.html')
def line_chart_dataset_detail(chart, dataset, div_id, idx):
    return {'title': chart.get_title(dataset),
            'color': chart.get_color(dataset),
            'div_id': div_id,
            'idx': idx}

