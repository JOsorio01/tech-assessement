from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core import models
from shows import serializers


class SimplePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class ShowViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShowSerializer
    queryset = models.Show.objects.all()
    pagination_class = SimplePagination

    def get_queryset(self):
        queryset = self.queryset

        title = self.request.query_params.get("title", None)

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DirectorSerializer
    queryset = models.Director.objects.all()
    pagination_class = SimplePagination

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get("name", None)

        if name:
            queryset = queryset.filter(director_name__icontains=name)

        return queryset.order_by("director_name")

class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActorSerializer
    queryset = models.Actor.objects.all()
    pagination_class = SimplePagination

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get("name", None)

        if name:
            queryset = queryset.filter(actor_name__icontains=name)

        return queryset.order_by("actor_name")

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
