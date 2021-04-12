from django import template

register = template.Library()


@register.filter
def view_rating(numb):
    """Removes all values of arg from the given string"""
    return int(numb) * '\u2605'
