from django import template

register = template.Library()

@register.filter(name='replace_value')
def replace_value(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, ' ')