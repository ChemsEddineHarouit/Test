from rest_framework import viewsets
from .serializers import BookSerializer, Book

class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer