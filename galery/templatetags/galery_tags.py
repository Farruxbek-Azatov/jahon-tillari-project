from django import template

register = template.Library()


@register.simple_tag
def img_url(event):
    images = event.images
    url = images.first().image.url
    return url
