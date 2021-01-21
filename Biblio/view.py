from django.views.generic import TemplateView
from django.urls import reverse

class homeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['authorListUrl'] = reverse('author:list') 
        ctx['bookListUrl'] = reverse('book:list') 
        return ctx
