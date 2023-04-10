from rest_framework import permissions

class IsPlantOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_authenticated and request.user == obj.partner 