from django.db import models
from django.urls import reverse
from Author.models import AuthorModel as Author


class BookManager(models.Manager):
    def get_filtered_queryset(self, queryset, filters):
        title = filters.get('title', None)
        author_name = filters.get('author_name', None)
        if title is not None:
            queryset = queryset.filter(models.Q(title__icontains = title))
        if author_name is not None:
            queryset = queryset.filter(models.Q(owner__name__icontains = author_name))
        return queryset

class BookModel(models.Model):
    title         = models.CharField(max_length=255, blank=False, null=False)
    owner         = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=False)
    cover         = models.ImageField(upload_to='book/covers', null=True, blank=True)

    objects = BookManager()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:detail', kwargs={'pk':self.pk})
    
    def get_update_url(self):
        return reverse('book:update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('book:delete', kwargs={'pk':self.pk})

    def get_author_url(self):
        return self.owner.get_absolute_url()

    

