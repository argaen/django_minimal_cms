from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models as django_models

from . import models


class BaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        django_models.TextField: {'widget': Textarea(attrs={'rows':50, 'cols':180})},
    }

class ContactInline(admin.StackedInline):
    model = models.Contact
    extra = 1

class AffiliationInline(admin.StackedInline):
    model = models.Affiliation
    extra = 1

class ResearcherAdmin(admin.ModelAdmin):
    inlines = (ContactInline, AffiliationInline,)


admin.site.register(models.Researcher, ResearcherAdmin)
admin.site.register(models.Article)
