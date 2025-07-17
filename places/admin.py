from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from tinymce.widgets import TinyMCE

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    fields = ('image', 'preview', 'number')
    readonly_fields = ('preview',)
    extra = 1

    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            img = format_html('<img src="{}" style="max-height:200px;max-width:200px"/>', obj.image.url)
            return img
        return "Изображение отсутсвует"
    preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
    search_fields = ['title']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['description_long'].widget = TinyMCE()
        return form


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    readonly_fields = ("preview",)
    autocomplete_fields = ['place']

    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            img = format_html('<img src="{}" style="max-height:200px;max-width:200px"/>', obj.image.url)
            return img
        return "Изображение отсутсвует"
    preview.short_description = "Превью"
