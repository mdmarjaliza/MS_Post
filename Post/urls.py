
from Post.api import PostsViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register(u'api/1.0/posts', PostsViewSet)

urlpatterns = router.urls



