from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        methods = ['PATCH', 'DELETE', 'POST']
        if request.method in methods:
            return request.user.is_staff
        elif request.method == 'GET':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        methods = ['PATCH', 'DELETE']
        if request.method in methods:
            return request.user
        elif request.method == 'GET':
            return True
        else:
            return False


class OwnerPermissionOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        methods = ['PATCH', 'DELETE']
        if request.method in methods:
            return request.user == obj or request.user.is_superuser
        elif request.method == 'GET':
            return True
        else:
            return False
