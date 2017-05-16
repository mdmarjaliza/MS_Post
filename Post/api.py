from django.utils.datetime_safe import datetime
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from Post.models import Post
from Post.serializers import PostsListsSerializer, PostsSerializer


# class PostsViewSet(ListModelMixin, GenericViewSet):
#     queryset = Post.objects.all().filter(publicate_at__lte=datetime.now()).order_by(
#         '-publicate_at').select_related("author")
#
#     serializer_class = PostsListsSerializer
#
#     renderer_classes = (TemplateHTMLRenderer,)
#     template_name = "post/home.html"
#     return Response({'posts': queryset})

# class PostsViewSet(APIView):
#     renderer_classes = (TemplateHTMLRenderer,)
#     template_name = "post/home.html"
#
#     def get(self, request):
#         queryset = Post.objects.all().filter(publicate_at__lte=datetime.now()).order_by(
#             '-publicate_at').select_related("author")
#         return Response({'posts': queryset})
#
#
# class CreatePostAPI(CreateAPIView):
#     """
#     Endpoint de creación de un nuevo post (solo usuarios autenticados)
#     """
#     # permission_classes = (IsAuthenticated,)
#
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer
#
#     def perform_create(self, serializer):
#         author = 0
#         return serializer.save(author=author)

# class CreatePostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#
#     def get_serializer_class(self):
#         return PostsSerializer if self.action == "create" else PostsListsSerializer
#
#     # def retrieve(self, request, *args, **kwargs):
#
#     def perform_create(self, serializer):
#         author = 0
#         return serializer.save(author=author)


class CreatePostViewSet(CreateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
