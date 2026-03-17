from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only the owner of an object can edit or delete it.
    Read-only access is allowed for everyone.
    """

    def has_object_permission(self, request, view, obj):
   
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user