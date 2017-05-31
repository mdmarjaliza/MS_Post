from django.conf.urls import url, include

from Categories import urls as categories_urls
from Post.api import PostsViewSet, UserPostsViewSet, PostDetailAPI


urlpatterns = [
    url(r'^api/1.0/posts', PostsViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts_list'),
    url(r'^api/1.0/userposts', UserPostsViewSet.as_view({'get': 'list'}), name='user_posts_list'),
    url(r'^api/1.0/postdetail', PostDetailAPI.as_view(), name='mspost_postdetail'),
    url(r'', include(categories_urls)),
]




