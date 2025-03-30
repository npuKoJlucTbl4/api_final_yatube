from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
