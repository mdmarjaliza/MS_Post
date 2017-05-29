from django.conf.urls import url

from Post.api import PostsViewSet, UserPostsViewSet

from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
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
    url(r'^api/1.0/posts', PostsViewSet, name='posts_list'),
    url(r'^api/1.0/userposts', UserPostsViewSet, name='user_posts_list'),
]