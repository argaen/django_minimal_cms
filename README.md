# Django Research Web

This package allows you to create single page websites with your research data (researchers, publications, etc.) and manage it. You can have multiple websites while keeping only a single database.

## How it works

To create a new Site you must create a new Project and assign it a Django site (the domain you will use for this site). When creating the new Project, you can assign sections to it naming them, setting their title, their content and the template you want to show.

### Adding new sections

Sections can be shared among your projects, you set the different parameters when assigning it to a Project. By itself, a section will only need a Title and a Page Content (explained later). When assigning the Section to your Project, you will be asked for:

    - order: Specifies the order of the section in your single page.
    - section: Which section you want to assign.
    - template: Which template (if any) you want to use. If you don't specify any, 'projects/templates/static.html' will be used.
    - content: If the section doesn't have a 'Page Content' associated, it means it is a static section, place here your content in markdown syntax and it will be displayed using static.html or the specified template.


### Adding new templates

To add a new template so you can use it with a section, you just need to create it and place it under 'your_app/templates' directory. This way, Django will find it automatically.

The variables that can be used in the template are:
    - order: Order of the section
    - title: Title of the section
    - objects: If the section has the 'page content' set, it is the queryset of the objects (resulting of doing page_content.objects.all(project=current_project, published=True)). If 'page content' is not set, it contains the static content.


#### Nesting templatetags

To add new templates, templatetags are used so the content returned from the view is rendered together with the template. The templatetag used for this is in 'projects/templatetags/project_tags.py' and is called 'build_section'.

Let's that rather than displaying all the objects belonging to a model you defined, you just want to display only the first 2 items ordered by an attribute called 'my_attribute'. You can do this defining your custom templatetag which will do the logic. Our template can be:

'''
{% get_highlights objects 2 as objects %}
{% for o in objects %}
    {{ o.my_attribute }}
{% endfor %}
'''

Now we have to create our 'your_app/templatetags/tags.py' file containing the 'get_highlights' templatetag which will perform the operations we want:

'''
@register.assignment_tag
def get_highlights(objects, n):
    return objects.order_by('my_attribute')[:n]
'''

### Adding new models

The 'page content' attribute when creating a new section refers to the dynamic data you want to display. If your section displays static data, you won't need this but in case you want to display dynamic data i.e. People of your team (which can be added, modified and deleted from the Django admin interface) you will need to set this attribute.

Your new added models, need to inherit from dynamic_cms.projects.GenericObject. This is because you need to mark your models as a class that can be used by the new sections.


## GenericObject Models

Researcher

Article
