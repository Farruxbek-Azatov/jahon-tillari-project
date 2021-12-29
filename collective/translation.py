from django.db.models import fields
from modeltranslation.translator import register, TranslationOptions
from .models import Category, Employee


@register(Category)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('position',)
