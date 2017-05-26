from django.utils.datetime_safe import datetime
from django.utils.encoding import smart_text
from rest_framework.authentication import get_authorization_header
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
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


# class PostsViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
#     def list(self, request, *args, **kwargs):
#         queryset = Post.objects.all().filter(publicated_at__lte=datetime.now()).order_by(
#             '-publicated_at').select_related("author")
#         serializer = PostsListsSerializer(queryset, many=True)
#         return Response(serializer.data)
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
#         return serializer.save(author=1)

# class PostsViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
#
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer
#
#     def perform_create(self, serializer):
#         return serializer.save()


# class PostsViewSet(ListModelMixin, GenericViewSet):
#     """
#     Endpoint que muestra la lista de posts
#     """
#
#     queryset = Post.objects.all().filter(publicated_at__lte=datetime.now()).order_by('-publicated_at')
#     serializer_class = PostsListsSerializer
#
#
# class CreatePostAPI(CreateAPIView):
#     """
#     Endpoint de creación de un nuevo post (solo usuarios autenticados)
#     """
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer
#
#     def perform_create(self, request, serializer):
#         auth_header = smart_text(get_authorization_header(request))
#         author_id = auth_header
#         return serializer.save(author=author_id)


# class PostsViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
#
#     def get_queryset(self, request):
#         if request.method == 'GET':
#             queryset = Post.objects.all().filter(publicated_at__lte=datetime.now()).order_by('-publicated_at')
#         elif request.method == 'POST':
#             queryset = Post.objects.all()
#         return queryset
#
#     def get_serializer_class(self, request):
#         if request.method == 'GET':
#             serializer_class = PostsListsSerializer
#         elif request.method == 'POST':
#             serializer_class = PostsSerializer
#         return serializer_class
#
#     def perform_create(self, request, serializer):
#         auth_header = smart_text(get_authorization_header(request))
#         author_id = auth_header
#         return serializer.save(author=author_id)

class PostsViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        auth_header = smart_text(get_authorization_header(self.request))
        author_id = int(auth_header)
        return serializer.save(author=author_id)
