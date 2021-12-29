from django import template
from ..models import Event

register = template.Library()


@register.simple_tag
def img_url(event):
    images = event.images
    url = images.first().image.url
    return url


@register.inclusion_tag('latest_events.html')
def show_latest_events(count=7):
    latest_events = Event.objects.all()[:count]
    return {'latest_events': latest_events}
