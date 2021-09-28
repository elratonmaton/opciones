from django.contrib import admin

from contact.models import ContactClients, ContactPage


class ContactClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'names', 'email', 'company_name')
    list_display_links = list_display


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'map_latitude', 'map_longitude', 'map_pin_title')
    list_display_links = list_display


admin.site.register(ContactClients, ContactClientsAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
