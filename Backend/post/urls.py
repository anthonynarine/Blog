from django.urls import path
# from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import PostViewset, UserViewset

router = SimpleRouter()
router.register("users", UserViewset, basename="users")
router.register("posts", PostViewset, basename="post")

urlpatterns = router.urls


# NOTE THIS WAS NEED WHEN generics
# urlpatterns = [
#     path("", PostList.as_view(), name="post_list"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
# ]