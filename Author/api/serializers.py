from rest_framework import serializers
from ..models import AuthorModel as Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']


