from django.contrib import admin
from . import models

class SectionInline(admin.TabularInline):
    model = models.Project.sections.through
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = (SectionInline,)


class TemplateAdmin(admin.ModelAdmin):
    list_filter = ('project',)

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Section)
admin.site.register(models.Researcher)
admin.site.register(models.Article)
admin.site.register(models.CTemplate, TemplateAdmin)
