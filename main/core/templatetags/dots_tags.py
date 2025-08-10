from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_dots(dots_class='1'):
    """
    Render dots with the specified class.
    Usage: {% render_dots '1' %}
    """
    context = {'dots_class': dots_class}
    return render_to_string('core/partials/dots.html', context)

@register.simple_tag
def render_multiple_dots(classes='1,2,3,4'):
    """
    Render multiple dots with specified classes.
    Usage: {% render_multiple_dots '1,2,3,4' %}
    """
    dots_classes = [cls.strip() for cls in classes.split(',')]
    html = ''
    for dots_class in dots_classes:
        context = {'dots_class': dots_class}
        html += render_to_string('core/partials/dots.html', context)
    return html
