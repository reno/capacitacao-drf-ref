from rest_framework import permissions


class UserAccessOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow the user to modify its data.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS or
            obj.id == request.user.id
        )