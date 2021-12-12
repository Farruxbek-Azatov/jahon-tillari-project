from django.contrib import admin
from .models import Category, Employee


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Employee)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'category', 'position')
    list_filter = ('category', 'position')
