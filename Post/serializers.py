from rest_framework import serializers

from Post.models import Post


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostsListsSerializer(PostsSerializer):
    class Meta(PostsSerializer.Meta):
        fields = ("title", "url_media", "intro", "fec_publicacion", "author")