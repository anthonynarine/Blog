from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    pagination_class = (IsAuthorOrReadOnly)
    queryset = Post.objects.all().order_by("created_at")
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    pagination_class = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    pagination_class = (IsAuthorOrReadOnly)
    querysetm = Post.objects.all()
    serializer_class = PostSerializer
