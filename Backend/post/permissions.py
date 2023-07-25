from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """Requires that a user be logged in or authenticated in order to have access"""
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_permission(self, request, view):
        # Read Permissions are allowed to any request we we'll always 
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissisons are only allowed to the author of a post
        return object.author == request.user