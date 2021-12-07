from rest_framework.permissions import BasePermission

class GroupPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Orsys').exists():
           return True
        return False

