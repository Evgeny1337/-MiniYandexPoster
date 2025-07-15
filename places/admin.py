from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from tinymce.widgets import TinyMCE


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    fields = ('image', 'preview', 'number')
    readonly_fields = ('preview',)
    extra = 1

    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            img = format_html(
                f'<img src="{
                    obj.image.url}" style="max-height:200px" />')
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
            img = format_html(
                f'<img src="{
                    obj.image.url}"  style="max-height:200px" />')
            return img
        return "Изображение отсутсвует"
    preview.short_description = "Превью"
