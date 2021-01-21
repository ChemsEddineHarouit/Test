from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import AuthorModel as Author
from .forms import AuthorForm
from Book.models import BookModel as Book

class AuthorListView(ListView):
    queryset = Author.objects.all()
    template_name = "Author/list.html"

class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    template_name = "Author/detail.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        author = ctx['object']
        ctx['books'] = Book.objects.filter(owner=author)
        return ctx

class AuthorCreateView(CreateView):
    template_name = "Author/create.html"
    form_class = AuthorForm


class AuthorUpdateView(UpdateView):
    queryset = Author.objects.all()
    template_name = "Author/update.html"
    form_class = AuthorForm

class AuthorDeleteView(DeleteView):
    queryset = Author.objects.all()
    template_name = "Author/delete.html"
    success_url = reverse_lazy('author:list')
