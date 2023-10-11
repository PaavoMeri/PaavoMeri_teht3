from django.contrib import admin
from .models import Kategoria, Kohde, UserType
from .models import SivunLataukset
class KohdeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'category', 'link')
    search_fields = ['name', 'ip_address', 'category__name']

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SivunLataukset)
class SivunLatauksetAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'ip_address']
    ordering = ['-timestamp']

admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Kohde, KohdeAdmin)
admin.site.register(UserType)
