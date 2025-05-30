from django.shortcuts import render
from .models import Omonim, Details
from .serializers import OmonimSerializer, DetailsSerializer

from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from rest_framework.filters import SearchFilter

@swagger_auto_schema(method='get', response={200: OmonimSerializer})
@api_view(['GET'])
def list_view(request):
    omonim = Omonim.objects.all()
    if omonim:
        response = OmonimSerializer(omonim, many=True)
        return Response(
            data=response.data,
            status=status.HTTP_200_OK
        )
    return Response({'message': 'Omonims not found'})



@swagger_auto_schema(method='get', response={200: DetailsSerializer})
@api_view(['GET'])
def detail_list_view(request):
    details = Details.objects.all()
    if details:
        response = DetailsSerializer(details, many=True)
        return Response(
            data=response.data,
            status=status.HTTP_200_OK
        )
    return Response({'message': 'Details not found'})


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description='Search by name', type=openapi.TYPE_STRING),
    ]
)
@api_view(['GET'])
def search_detail_view(request):
    name = request.GET.get('name', '').strip()
    queryset = Omonim.objects.all()

    if name:
        queryset = queryset.filter(name__icontains=name)

    serializer = OmonimSerializer(queryset, many=True)
    return Response(serializer.data)


class Post_omonim(CreateAPIView):
    queryset = Omonim.objects.all()
    serializer_class = OmonimSerializer
    permission_classes = [IsAuthenticated]

class Post_detail(CreateAPIView):
    queryset = Details.objects.all()
    serializer_class = OmonimSerializer
    permission_classes = [IsAuthenticated]

