
from django.views.generic.base import TemplateView


class Author(TemplateView):
    template_name = 'about/author.html'
