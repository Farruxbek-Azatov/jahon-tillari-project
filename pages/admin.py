from django.contrib import admin
from .models import Person

admin.site.site_header = 'Jahon tillari litseyi'
admin.site.site_title = 'Jahon tillari litseyi'
admin.site.index_title = 'Sayt adminstratsiyasi'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone',
                    'created', 'answered')
    list_filter = ('subject', 'created', 'answered')
    search_fields = ('subject', 'message', 'phone')
    ordering = ('-created',)
