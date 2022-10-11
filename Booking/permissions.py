from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from rest_framework.request import Request


class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request: Request, view):
        is_admin = super(IsAdminUserOrReadOnly, self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin
