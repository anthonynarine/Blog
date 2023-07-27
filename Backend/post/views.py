from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model

# NOTE converted to viewsets from generics class based views

class PostViewset(viewsets.ModelViewSet):
    """
    PostList is a viewset that provides the default create(), retrieve(), update(),
    partial_update(), destroy() and list() actions for the Post model.
    It orders the posts by the time they were created.
    It also applies the IsAuthorOrReadOnly permission to all the operations.
    """

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all().order_by("created_at")
    serializer_class = PostSerializer


class UserViewset(viewsets.ModelViewSet):
    """
    PostDetail is a viewset that provides the default create(), retrieve(), update(),
    partial_update(), destroy() and list() actions for the User model.
    """
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


"""In Django Rest Framework, you have different levels of abstraction to implement your API views. The two main abstraction levels are Generic views and Viewsets.

Generic views (like generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView, etc.) are class-based views that come with predefined functions for handling HTTP verbs like GET, POST, PUT, DELETE, etc. They are used when you want to provide a specific set of functionalities on a model (for example, List and Create, or Retrieve, Update and Destroy).

The Viewsets classes (like viewsets.ModelViewSet) on the other hand, provide a way to combine the logic for a set of related views in a single class. A ModelViewSet will provide the complete set of default read and write operations (GET, POST, PUT, PATCH, DELETE).

The main differences between them:

Abstraction Level: Viewsets are higher level of abstraction compared to generic views. They automatically implement default operations without you having to specify them.

Routing: If you use viewsets and routers, you don't need to manually wire up the URL conf. The router classes handle it automatically. With generic views, you have to manually set up your URLs.

Use Case: If you are dealing with standard CRUD operations, viewsets can speed up development. But if you need more granular control and customization, using generic views can be more beneficial.

So, it largely depends on what your use case is. If you need the complete set of operations and you want to take advantage of automatic URL routing, using viewsets.ModelViewSet would be a good choice. If you need to provide only specific set of functionalities or you need more control over the flow, generic views might be a better fit."""


