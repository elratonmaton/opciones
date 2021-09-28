from django.contrib import admin

from company.models import Slider, Company


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'heading')
    list_display_links = list_display


admin.site.register(Slider, SliderAdmin)
admin.site.register(Company, CompanyAdmin)
