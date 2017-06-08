import json

from django.db.models import Q
from django.utils.datetime_safe import datetime
from django.utils.encoding import smart_text
from rest_framework.authentication import get_authorization_header
from rest_framework.decorators import authentication_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from Post.models import Post
from Post.permissions import PostDetailPermission
from Post.serializers import PostsSerializer, PostsListsSerializer
from Post.auth import JSONAuthentication
from django.db.models import Q


class PostsViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Post.objects.all().filter(Q(publicated_at__lte=datetime.now()) & Q(state='PUB')).order_by(
                '-publicated_at')
        elif self.request.method == 'POST':
            queryset = Post.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = PostsListsSerializer
        elif self.request.method == 'POST':
            serializer_class = PostsSerializer
        return serializer_class

    def perform_create(self, serializer):

        authentication_classes(JSONAuthentication, )
        # Ahora la cabecera de Authentication pasa el id del autor y su username, así que estas líneas siguientes no
        # no hacen falta:
        # auth_header = smart_text(get_authorization_header(self.request))
        # author_id = int(auth_header)
        # author_username = self.request.META.get('HTTP_X_USERNAME')

        # en estas dos líneas siguiente cogemos las cabeceras y las convertimos a un json
        auth_header = smart_text(get_authorization_header(self.request))
        user_data = json.loads(auth_header)

        return serializer.save(author=user_data.get('id'), author_username=user_data.get('username'))


class UserPostsViewSet(ListModelMixin, GenericViewSet):
    """
    Endpoint que muestra la lista de posts en el blog de un usuario
    """

    serializer_class = PostsListsSerializer

    def get_queryset(self):
        blogger = self.request.META.get('HTTP_XBLOGGER')
        blogger_id = int(self.request.META.get('HTTP_XBLOGGERID'))
        if self.request.user.is_authenticated and (
                        self.request.user.username == blogger or self.request.user.is_superuser):
            queryset = Post.objects.all().filter(author=blogger_id).order_by(
                '-publicated_at')
        else:
            queryset = Post.objects.all().filter(
                Q(author=blogger_id) & Q(state='PUB') & Q(publicated_at__lte=datetime.now())).order_by(
                '-publicated_at')
        return queryset


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint que muestra el detalle de un post
    """

    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (PostDetailPermission,)

    def retrieve(self, request):
        blogger = self.request.META.get('HTTP_X_BLOGGER')
        post_id = int(self.request.META.get('HTTP_X_POSTID'))
        post = get_object_or_404(Post, pk=post_id, author_username=blogger)
        self.check_object_permissions(request, post)
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    def perform_update(self, serializer):
        if not self.request.user.is_superuser:
            return serializer.save(author=self.request.user.pk, author_username=self.request.user.username)
        else:
            return serializer.save()


class CategoryPostsViewSet(ListModelMixin, GenericViewSet):
    """
    Endpoint que muestra la lista de posts por categoria
    """

    serializer_class = PostsListsSerializer

    def get_queryset(self):
        category = int(self.request.META.get('HTTP_X_CATEGORY'))
        queryset = Post.objects.all().filter(
            Q(category__id=category) & Q(state='PUB') & Q(publicated_at__lte=datetime.now())).order_by(
            '-publicated_at')
        return queryset