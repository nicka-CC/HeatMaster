from django.contrib import admin
from .models import Thermostats, Thermostat, ThermostatImages, HeatedMats, Blog, ImageBlog, Part, WarmFloor, ModelRange, \
    MethodPay, Produce, HistoryApplication, Applications, History, HotCable, LetsCooperate, CalculatePrice, CommentBlog


class ThermostatsAdmin(admin.ModelAdmin):
    list_display = ('type', 'icon_preview')

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"

class ThermosatImageAdmin(admin.TabularInline):
    model = ThermostatImages
    extra = 1
class ThermostatAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview')

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"
    inlines = [ThermosatImageAdmin]

class ImageBlogInline(admin.TabularInline):
    model = ImageBlog
    extra = 1
class CommentsBlogInline(admin.TabularInline):
    model = CommentBlog
    extra = 1
class BlogAdmin(admin.ModelAdmin):
    inlines = [ImageBlogInline, CommentsBlogInline]

class PartAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview')

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"

class WarmFloorAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview')

    def icon_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="50" height="50" style="border-radius: 5px;"/>'
        elif  obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"

class MethodPayAdmin(admin.ModelAdmin):
    list_display = ('icon', 'icon_preview')

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"

class ProduceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'icon_preview')

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"

class HistoryApplicationAdmin(admin.TabularInline):
    model = HistoryApplication
    extra = 1
class ApplicationsAdmin(admin.ModelAdmin):
    inlines = [HistoryApplicationAdmin]

class HotCableAdmin(admin.ModelAdmin):
    list_display = ('image', 'icon_preview')

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px;"/>'
        return "Нет изображения"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Превью"
admin.site.register(Thermostats, ThermostatsAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
admin.site.register(HeatedMats)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(WarmFloor, WarmFloorAdmin)
admin.site.register(ModelRange)
admin.site.register(MethodPay, MethodPayAdmin)
admin.site.register(Produce, ProduceAdmin)
admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(History)
admin.site.register(HotCable, HotCableAdmin)
admin.site.register(LetsCooperate)
admin.site.register(CalculatePrice)