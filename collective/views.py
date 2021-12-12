from django.shortcuts import get_object_or_404, render
from .models import Category


def employee(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'collective/page.html',
                  {'category': category})
