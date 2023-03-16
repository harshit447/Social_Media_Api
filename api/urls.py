from django.urls import path
from .views import (
    get_user_profile,
    follow_user,
    unfollow_user,
    upload_post,
    get_or_delete_post,
    like_post,
    unlike_post,
    comment_on_post,
    user_detail,
    all_posts,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('user/', user_detail),
    path('user/<int:user_id>/profile', get_user_profile),
    path('user/<int:user_id>/follow', follow_user),
    path('user/<int:user_id>/unfollow', unfollow_user),
    path('posts/', upload_post),
    path('all-posts/', all_posts),
    path('posts/<int:post_id>/', get_or_delete_post),
    path('like/<int:post_id>/', like_post),
    path('unlike/<int:post_id>/', unlike_post),
    path('comment/<int:post_id>/', comment_on_post),
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
