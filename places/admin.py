from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableTabularInline, SortableAdminMixin, SortableAdminBase
from tinymce.widgets import TinyMCE

class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    fields = ('image','preview','number')
    readonly_fields = ('preview',)
    extra = 1

    def preview(self, obj):
        if obj.image and hasattr(obj.image,'url'):
            return mark_safe(f'<img src="{obj.image.url}" height="200" />')
        return "Изображение отсутсвует"
    preview.short_description = "Превью"

@admin.register(Place)
class PlaceAdmin(SortableAdminBase,admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['description_long'].widget = TinyMCE()
        return form
    

    
@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    readonly_fields = ("preview",)
    def preview(self, obj):
        if obj.image and hasattr(obj.image,'url'):
            return mark_safe(f'<img src="{obj.image.url}" height="200" />')
        return "Изображение отсутсвует"
    preview.short_description = "Превью"

