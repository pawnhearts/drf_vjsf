from django.shortcuts import render
from rest_framework import viewsets, pagination
from rest_framework.decorators import action

from .models import *
from .serializers import get_serializer_class, BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["state"]
    pagination_class = pagination.PageNumberPagination

    @action(detail=False, methods=['GET'])
    def html(self, request):
        return render(request, 'vue_form.html', {})

    @action(detail=True, methods=['GET'], url_path='html')
    def html_detail(self, request, pk):
        return render(request, 'vue_form.html', {'pk': pk})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = pagination.LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def html(self, request):
        return render(request, 'vue_form.html', {})



class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = get_serializer_class(Publisher)

