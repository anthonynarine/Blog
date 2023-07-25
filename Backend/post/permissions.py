from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a post to edit it.
    Other authenticated users only have read permissions.
    """

    def has_permission(self, request, view):
        """
        Checks whether the user is authenticated, allowing access 
        to any authenticated user 
        
        Parameters:
        request (rest_framework.request.Request): Standard DRF request object.
        view (rest_framework.views.View): Standard DRF view object.

        Returns:
        bool: True if the user is authenticated, else False
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check.

        Allow GET, HEAD, or OPTIONS requests for any user (authenticated or not).
        Only allow edits (PUT, PATCH, DELETE) if the post is authored by the
        user making the request.

        Parameters:
        request (rest_framework.request.Request): Standard DRF request object.
        view (rest_framework.views.View): Standard DRF view object.
        obj (Post): The post object that is being accessed.

        Returns:
        bool: True if permission is granted, else False
        """
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
