from django.http import request
from django.shortcuts import render
from django.views.generic.base import View, TemplateResponseMixin

import pages


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def apply_page(request):
    return render(request, 'pages/apply_page.html')
