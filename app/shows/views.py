from rest_framework import viewsets

from core.models import Show
from shows.serializers import ShowSerializer


class ShowViewSet(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
