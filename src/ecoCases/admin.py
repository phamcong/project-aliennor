from django.contrib import admin
from .models import EcoCase, ESM
# Register your models here.


class ESMInline(admin.TabularInline):
    model = ESM
    extra = 2


class EcoCaseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['ecocase_title',
                           'ecocase_description', 'ecocase_characters']}),
        ('Date information', {'fields': ['timestamp']})
    ]
    inlines = [ESMInline]
    list_display = ['ecocase_title', 'timestamp']
    list_filter = ['timestamp']


admin.site.register(EcoCase, EcoCaseAdmin)
admin.site.register(ESM)
