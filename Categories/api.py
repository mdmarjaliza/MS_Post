from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from Categories.models import Category
from Categories.serializers import CategorySerializer


class CategoryViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Category.object.all()
    serializer_class = CategorySerializer
