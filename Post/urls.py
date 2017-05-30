from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from Post.api import PostsViewSet, UserPostsViewSet, PostDetailAPI

# router = DefaultRouter()
# router.register('api/1.0/blogs/(?P<blogger>[a-z0-9_-]+)', UserPostsViewSet, base_name='api_user_posts')
#
#
# # router.register(u'api/1.0/posts', PostsViewSet, base_name='posts_')
# # router.register(u'api/1.0/create', CreatePostAPI)
#
#
# urlpatterns = [
# #     #conexion al microservicio de posts
#     url(u'api/1.0/posts', PostsViewSet, name='posts_'),
#     url(u'api/1.0/userposts', UserPostsViewSet, name='user_posts_list_')
# #     url(u'api/1.0/create', CreatePostAPI.as_view(), name=
# #     router.urls
#  ]
#
# # urlpatterns = router.urls
urlpatterns = [
    url(r'^api/1.0/posts', PostsViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts_list'),
    url(r'^api/1.0/userposts', UserPostsViewSet.as_view({'get': 'list'}), name='user_posts_list'),
    url(r'^api/1.0/postdetail', PostDetailAPI.as_view(), name='mspost_postdetail'),


]