from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from Author.models import AuthorModel as Author
from .models import BookModel as Book
from .forms import BookForm

class BookListView(ListView):
    paginate_by = 3
    template_name = "Book/list.html"
    def get_queryset(self, *args, **kwargs):
        filter_params = self.request.GET
        print(filter_params)
        queryset = Book.objects.all().order_by('title')
        queryset = Book.objects.get_filtered_queryset(queryset, filter_params)
        return queryset

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = "Book/detail.html"

class BookCreateView(CreateView):
    template_name = "Book/create.html"
    form_class = BookForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(BookCreateView, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Book()
        kwargs['instance'].owner = Author.objects.get(pk=self.kwargs['owner'])
        return kwargs


class BookUpdateView(UpdateView):
    queryset = Book.objects.all()
    template_name = "Book/update.html"
    form_class = BookForm

class BookDeleteView(DeleteView):
    queryset = Book.objects.all()
    template_name = "Book/delete.html"
    
    def get_success_url(self, *args, **kwargs):
        book = self.object
        return book.get_author_url()
