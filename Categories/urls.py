from django.conf.urls import url

from Categories.api import CategoryViewSet

urlpatterns = [
    url(r'^api/1.0/categories', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='categories')
]