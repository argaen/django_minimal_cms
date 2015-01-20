from django.db import models
from django.utils.translation import ugettext_lazy as _

from djzone_cms.models import GenericObject
from filer.fields.image import FilerImageField


class Researcher(GenericObject):

    name = models.CharField(_("Name"), max_length=20)
    last_name = models.CharField(_("Last name"), max_length=20)
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)

    twitter = models.CharField(_("Twitter"), max_length=30, null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    researcher = models.ForeignKey(Researcher, verbose_name=_("Researcher"))
    department = models.CharField(_("Department"), max_length=200, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=200)
    city = models.CharField(_("City"), max_length=100)
    state = models.CharField(_("State"), max_length=100)
    zip_code = models.CharField(_("Zip code"), max_length=100)
    country = models.CharField(_("Country"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.address


class Affiliation(models.Model):
    researcher = models.ForeignKey(Researcher, verbose_name=_("Researcher"))
    category = models.CharField(_("Category"), max_length=100)
    institution = models.CharField(_("Institution"), max_length=200)

    def __unicode__(self):
        return self.institution


class Article(GenericObject):

    title = models.CharField(_("Title"), max_length=500)
    abstract = models.TextField(_("Abstract"))
    doi = models.CharField(_("DOI"), max_length=50)
    authors = models.CharField(_("Authors"), max_length=500)

    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)

    published_on = models.DateField(_("Published on"))
    journal = models.CharField(_("Journal"), max_length=500)
    volume = models.CharField(_("volume"), max_length=100, blank=True)
    first_page = models.CharField(_("First page / Article #"), max_length=20)
    last_page = models.CharField(_("Last page"), max_length=20, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-published_on',)
