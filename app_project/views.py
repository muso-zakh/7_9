from django.shortcuts import render
from .models import Category, Term
from .serializers import CategorySerializer, TermSerializer

from rest_framework.pagination import PageNumberPagination

from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from rest_framework.filters import SearchFilter



@swagger_auto_schema(method='get', response={200: CategorySerializer})
@api_view(['GET'])
def list_view(request):
    category = Category.objects.all()
    if category:
        response1 = CategorySerializer(category, many=True)
        response2 = TermSerializer(Term.objects.all(), many=True)
        return Response(
            data={"category":response1.data,  "term":response2.data}, 
            status=status.HTTP_200_OK
        )
    return Response({'message': 'Category not found'})



@swagger_auto_schema(method='get', response={200: TermSerializer})
@api_view(['GET'])
def detail_list_view(request):
    term = Term.objects.all()
    if term:
        response = TermSerializer(term, many=True)
        return Response(
            data=response.data,
            status=status.HTTP_200_OK
        )
    return Response({'message': 'Term not found'})


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description='Search by name', type=openapi.TYPE_STRING),
    ]
)
@api_view(['GET'])
def search_category_view(request):
    name = request.GET.get('name', '')
    queryset = Category.objects.all()

    if name:
        queryset = queryset.filter(name__icontains=name)


    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_id_view(request, pk):
    try:
        detail = Term.objects.get(pk=pk)
    except Term.DoesNotExist:
        return Response({'error': 'Detail not found'}, status=404)
    
    term_serializer = TermSerializer(detail)

    
    related_terms_qs = Term.objects.filter(category=detail.category).exclude(id=detail.id)[:20]
    related_terms_serializer = TermSerializer(related_terms_qs, many=True)

    return Response({
        'term': term_serializer.data,
        'related_terms': related_terms_serializer.data
    })

    # serializer = TermSerializer(detail)
    # return Response(serializer.data)

class TermPagination(PageNumberPagination):
    page_size = 2

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('word', openapi.IN_QUERY, description='Search by word, definition, id', type=openapi.TYPE_STRING),
        openapi.Parameter('page', openapi.IN_QUERY, description='Page number', type=openapi.TYPE_INTEGER),
    ]
)
    
@api_view(['GET'])
def detail_ordering(request):
    word = request.GET.get('word', '')
    queryset = Term.objects.all()

    if word:
        queryset = queryset.order_by(word)


    paginator = TermPagination()
    page = paginator.paginate_queryset(queryset, request)
    serializer = TermSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)




@swagger_auto_schema(method='post', request_body=CategorySerializer())
@api_view(['POST'])
def create_category_view(request):
    category = CategorySerializer(data=request.data)
    if category.is_valid():
        category.save()
        return Response(
            category.data,
            status=status.HTTP_201_CREATED
        )
    return Response({'error': category.errors})


@swagger_auto_schema(method='post', request_body=TermSerializer())
@api_view(['POST'])
def create_term_view(request):
    term = TermSerializer(data=request.data)
    if term.is_valid():
        term.save()
        return Response(
            term.data,
            status=status.HTTP_201_CREATED
        )
    return Response({'error': term.errors})


