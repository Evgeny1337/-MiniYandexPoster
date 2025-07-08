from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    field = ('image','preview')
    readonly_fields = ('preview',)
    extra = 1
    def preview(self, obj):
        if obj.image and hasattr(obj.image,'url'):
            return mark_safe(f'<img src="{obj.image.url}" height="200" />')
        return "Изображение отсутсвует"
    preview.short_description = "Превью"

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
    
@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image and hasattr(obj.image,'url'):
            return mark_safe(f'<img src="{obj.image.url}" height="200" />')
        return "Изображение отсутсвует"
    preview.short_description = "Превью"

