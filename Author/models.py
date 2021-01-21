from django.db import models
from django.urls import reverse

class AuthorModel(models.Model):
    name         = models.CharField(max_length=255, blank=False, null=False)
    birth_date   = models.DateField(blank=False, null=False)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author:detail', kwargs={'pk':self.pk})
    
    def get_update_url(self):
        return reverse('author:update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('author:delete', kwargs={'pk':self.pk})

    def get_create_book_url(self):
        return reverse('author:create-book', kwargs={'owner':self.pk})