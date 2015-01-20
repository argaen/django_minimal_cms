# Django Minimal CMS

This package allows you to manage various projects on a different Django site each. Those sites are single web pages. Each project has their sections with an assigned template to render and display the content (static or not).

The content type to be rendered can be selected in the section administration page (actually only 1 is allowed). When selecting a content type, you are turning the section into a dynamic html page so, to use the dynamic content, in the template you can use the 'objects' variable which is a queryset of the selected content type.

You can use any tag you want in the templates content, just remember to use the {% load %} tag whenever is needed.


## Getting started

Create a new Django project with `django-admin.py startproject <yourproject>`. Install the package with `pip install django_zonecms` and add it to INSTALLED_APPS in your settings.py file with 'djzone_cms' name. Do a `python manage.py syncdb` to create the database and migrate the package models into it. Now you can start the development server to create a new project with its sections and templates `python manage.py runserver`.

You also need to add some other applications, your INSTALLED_APPS should end like that:

```python
INSTALLED_APPS = (
    .
    .
    .
    
    'django.contrib.sites',

    'polymorphic',
    'django.contrib.contenttypes',

    'filer',
    'mptt',
    'easy_thumbnails',
    'djzone_cms'
)
```

Note that we added the 'django.contrib.sites' and moved 'django.contrib.contenttypes' under the 'polymorphic' app. You should also add the `SITE_ID=1` line into your settings.py file.

## Creating a new project

Add a new project using the admin interface and fullfill the required fields. An important one is the 'base_template' where you must write your root html template. You can see an example running the test server under examples/ and accessing the admin interface. In the example, one of the most important parts is:

```
{% for section in project.sectionorder_set.all %}
    {% build_section section %}
{% endfor %}
```

To be able to execute this lines, you must load the associated templatetag at the top of the template with `{% load project_tags %}`. This lines are the ones that pick all the sections of the project and build them obtaining the dynamic or static referred content and rendering the specific template of each section with it.

Next step is to add new sections and assign them their own templates. The content type you can assign to a section is any class that inherits from the 'zone_cms.projects.models.GenericObject' class so, if you want to write your own to display them in your sections, don't forget to use 'GenericObject' as a parent class. You can also write your own templatetags so you can use them while writing your templates in the admin interface.


## Creating custom models

To create new models nothing changes from the normal way of working with Django, the only thing you have to do is to make your models (the ones you want to be able to select for your sections) inherit from 'GenericObject' class.

For static files, templatetags and rest, you can work the normal way you do with Django.


## Displaying the contents

To display the single page, you will need to add this line in your main urls.py file:

```python
    url(r'^$', 'djzone_cms.views.home', name='home'),
```
