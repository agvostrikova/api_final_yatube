from django.urls import include, path

from rest_framework import routers

from .views import (
    GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet
)


v1_router = routers.DefaultRouter()

v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)


urlpatterns = [
    path(
        'v1/',
        include(
            [
                path('', include('djoser.urls.jwt')),
                path('', include(v1_router.urls)),
            ]
        ),
    ),
]
