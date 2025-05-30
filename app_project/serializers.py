from rest_framework.serializers import ModelSerializer
from .models import Omonim, Details

class OmonimSerializer(ModelSerializer):
    class Meta:
        model = Omonim
        fields = '__all__'
        read_only_fields = ['id']


class DetailsSerializer(ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'
        read_only_fields = ['id']