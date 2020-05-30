from django.contrib import admin
from restaurant import models


# Register your models here.

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MenuCategory, MenuCategoryAdmin)
