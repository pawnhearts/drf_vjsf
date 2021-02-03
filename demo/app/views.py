from django.shortcuts import render
from rest_framework import viewsets, pagination
from rest_framework.decorators import action

from drf_jsonschema import to_jsonschema
from rest_framework.response import Response

from .models import *
from .serializers import get_serializer_class, BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["state"]
    pagination_class = pagination.PageNumberPagination

    @action(detail=False, methods=['GET'])
    def schema(self, request):
        return Response(to_jsonschema(self.get_serializer()))



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = pagination.LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def schema(self, request):
        return Response(to_jsonschema(self.get_serializer()))


    @action(detail=False, methods=['GET'])
    def html(self, request):
        return render(request, 'authors.html', {})


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = get_serializer_class(Publisher)

