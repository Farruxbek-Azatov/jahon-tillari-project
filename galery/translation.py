from modeltranslation.translator import register, TranslationOptions
from .models import Event


@register(Event)
class PostTranslationOptions(TranslationOptions):
    fields = ('title',)
