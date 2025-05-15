from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    - SAFE_METHODS (GET, HEAD, OPTIONS) are allowed to anyone.
    - POST is allowed to anyone (e.g., user registration).
    - Other methods (PUT, PATCH, DELETE) require the user to be authenticated and the owner of the object.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj
