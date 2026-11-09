from django.contrib import admin

from .models import LivreDorEntry, Soiree


@admin.register(Soiree)
class SoireeAdmin(admin.ModelAdmin):
    list_display = ['titre', 'date', 'lieu']
    search_fields = ['titre', 'lieu']
    date_hierarchy = 'date'


@admin.register(LivreDorEntry)
class LivreDorEntryAdmin(admin.ModelAdmin):
    list_display = ['nom', 'auteur', 'message', 'created_at', 'is_visible']
    list_editable = ['is_visible']
    list_filter = ['is_visible', 'auteur']
    search_fields = ['nom', 'message', 'auteur__username']
    actions = ['approve', 'hide']

    @admin.action(description='Rendre visibles')
    def approve(self, request, queryset):
        queryset.update(is_visible=True)

    @admin.action(description='Masquer')
    def hide(self, request, queryset):
        queryset.update(is_visible=False)
