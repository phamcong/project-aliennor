from django.contrib import admin
from .models import EcoCase, ESM
from django.forms import TextInput, Textarea
from django.db import models
from .forms import EcoCaseForm
# Register your models here.


class ESMInline(admin.TabularInline):
    model = ESM
    extra = 0


class EcoCaseAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
    # }
    fieldsets = [
        (None, {'fields': ['user', 'ecocase_title',
                           'ecocase_description', 'ecocase_characters', 'ecocase_images', 'ecocase_image_urls']}),
        ('Date information', {'fields': ['timestamp']})
    ]
    inlines = [ESMInline]
    list_display = ['ecocase_title', 'timestamp']
    list_filter = ['timestamp']


admin.site.register(EcoCase, EcoCaseAdmin)
admin.site.register(ESM)
