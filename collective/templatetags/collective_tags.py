from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('pages/r.html')
def all_categories():
    categories = Category.objects.all()
    return {'categories': categories}
