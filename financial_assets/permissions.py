from rest_framework import permissions


class IsWalletOwner(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        return obj.user == request.user


class IsWalletOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        return request.user.is_superuser or obj.user == request.user
