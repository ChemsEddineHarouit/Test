from rest_framework import viewsets
from .serializers import AuthorSerializer, Author

class AuthorAPIViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer