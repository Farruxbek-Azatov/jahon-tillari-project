from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import PersonForm


def index(request):
    return render(request, 'pages/index.html', {'active': 'home'})


def about(request):
    return render(request, 'pages/about.html', {'active': 'about'})


def contact(request):
    return render(request, 'pages/contact.html', {'active': 'contact'})


@require_POST
def check(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': _("Sizning xabaringiz jo'natildi")})
    return JsonResponse({'status': _("Xato! Qayta urinib ko'ring")})


def apply_page(request):
    return render(request, 'pages/apply_page.html', {'active': 'apply'})
