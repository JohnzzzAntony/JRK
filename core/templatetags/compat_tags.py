from django import template

register = template.Library()

@register.filter(name='length_is')
def length_is_compat(value, arg):
    """Restores the length_is filter for Jazzmin compatibility on Django 5.1/5.2"""
    try:
        if value is None:
            return False
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return False
