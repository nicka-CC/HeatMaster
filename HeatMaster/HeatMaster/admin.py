from django.contrib import admin
from .models import Thermostats

class ThermostatsAdmin(admin.ModelAdmin):
    list_display = ('type', 'icon_preview')  # Добавляем кастомное поле для превью изображения

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"

admin.site.register(Thermostats, ThermostatsAdmin)
