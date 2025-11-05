from rest_framework import permissions 

class IsAdminReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool (request.user and request.user.is_active)

class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET']=['%(app_level)s.view_%(model_name)s']