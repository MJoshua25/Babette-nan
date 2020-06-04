from django.contrib import admin
from restaurant import models


# Register your models here.

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
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


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
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


class PlatAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'prix',
        'category',
        'ingredients',
        'isRecommended',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
                'prix',
                'categorie',
                'ingredients'
            ]
        }),
        ('Recommendation', {
            'fields': [
                'isRecommended',
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
_register(models.Ingredient, IngredientAdmin)
_register(models.Plat, PlatAdmin)
