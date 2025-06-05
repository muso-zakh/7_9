from rest_framework.serializers import ModelSerializer
from .models import Category, Term



class TermSerializer(ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'
        read_only_fields = ['id']


class CategorySerializer(ModelSerializer):
    details = TermSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

