from django.conf.urls import url

from Post.api import PostsViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register(u'api/1.0/posts', PostsViewSet, base_name='posts_')
# router.register(u'api/1.0/create', CreatePostAPI)


# urlpatterns = [
#     #conexion al microservicio de posts
#     url(u'api/1.0/list', PostsViewSet, name='posts_list'),
#     url(u'api/1.0/create', CreatePostAPI.as_view(), name='create_post'),
# ]

urlpatterns = router.urls
