from rest_framework.serializers import ModelSerializer
from .models import Category, Term

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']


class TermSerializer(ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'
        read_only_fields = ['id']