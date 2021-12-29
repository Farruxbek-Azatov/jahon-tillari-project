from django.shortcuts import get_object_or_404, render
from .models import Event


def event_list(request):
    events = Event.objects.all()
    return render(request, 'galery/list.html', {'events': events, 'active': 'galery'})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'galery/detail.html', {'event': event, 'active': 'galery'})
