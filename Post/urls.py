from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

# from Post.views import HomeView, UserPostsView, CategoryPostsView
from Post.api import CreatePostViewSet
# from Post.views import PostsViewSet
# from Post.views import HomeView

router = SimpleRouter()
# router.register('api/1.0/blogs/(?P<blogger>[a-z0-9_-]+)', UserPostsViewSet, base_name='api_user_posts')
router.register(r'new-post', CreatePostViewSet)

# urlpatterns = [
#     #Web URLs
#     url(r'^$', HomeView.as_view(), name='post_home'),
#     url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/$', UserPostsView.as_view(), name='post_usersposts'),
#     # url(r'^categorias/(?P<category>[a-z0-9_-]+)/$', CategoryPostsView.as_view(), name='post_categoryposts'),
#
#     #API URLs
#
#     url('', include(router.urls))
# ]

urlpatterns = router.urls
