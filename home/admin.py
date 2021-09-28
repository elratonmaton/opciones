from django.contrib import admin

from home.models import Slider, AboutUs, Mision, Vision, SocialResponsability


class SlidersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')
    list_display_links = list_display


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


class MisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = list_display


class VisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = list_display


class SocialResponsabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


admin.site.register(Slider, SlidersAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(SocialResponsability, SocialResponsabilityAdmin)
