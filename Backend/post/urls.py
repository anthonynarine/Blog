from django.urls import path
# from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import PostViewset, UserViewset

router = DefaultRouter()
router.register("users", UserViewset, basename="users")
router.register("posts", PostViewset, basename="post")

urlpatterns = router.urls


# NOTE THIS WAS NEED WHEN generics class based views
# urlpatterns = [
#     path("posts/", PostList.as_view(), name="post_list"),
#     path("posts/<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("users/", UserList.as_view(), name="user_list"),
#     path("users/<int:pk>/", UserDetal.as_view(), name="user_detal"),
# ]