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
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ESMInline]
    list_display = ['ecocase_title', 'pub_date']
    list_filter = ['pub_date']


admin.site.register(EcoCase, EcoCaseAdmin)
admin.site.register(ESM)
