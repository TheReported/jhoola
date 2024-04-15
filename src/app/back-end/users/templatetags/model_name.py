from django import template

register = template.Library()


@register.filter
def check_model_name(obj, attr):
    return obj._meta.model_name == attr
