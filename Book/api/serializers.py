from rest_framework import serializers
from ..models import BookModel as Book
from Author.api.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    owner = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['title', 'owner']


