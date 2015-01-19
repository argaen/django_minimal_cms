from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models as django_models

from . import models


class BaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        django_models.TextField: {'widget': Textarea(attrs={'rows':50, 'cols':180})},
    }

class SectionInline(admin.TabularInline):
    model = models.Project.sections.through
    extra = 0

class ProjectAdmin(BaseAdmin):
    inlines = (SectionInline,)
    list_display = ('title', 'subtitle', 'site')


class TemplateAdmin(BaseAdmin):
    list_filter = ('project',)


class SectionAdmin(BaseAdmin):
    list_display = ('title', 'content_type')
    list_filter = ('project',)
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Theme', {
            'fields': ('icon', 'background_color', 'background_image')
        }),
        ('Data', {
            'fields': ('content_type',)
        }),
    )

class ContactInline(admin.StackedInline):
    model = models.Contact
    extra = 1

class AffiliationInline(admin.StackedInline):
    model = models.Affiliation
    extra = 1

class ResearcherAdmin(admin.ModelAdmin):
    inlines = (ContactInline, AffiliationInline,)

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.Researcher, ResearcherAdmin)
admin.site.register(models.Article)
admin.site.register(models.CTemplate, TemplateAdmin)
