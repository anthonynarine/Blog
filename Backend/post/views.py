from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("created_at")
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# this permission class will not allow logged out users to view post
# logged in users can view the list page, but only admin users can see the  detial page
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser)
    querysetm = Post.objects.all()
    serializer_class = PostSerializer
