from django import template
register = template.Library()


@register.assignment_tag
def get_highlights(objects, n):
    return objects.exclude(image=None)[:n]
