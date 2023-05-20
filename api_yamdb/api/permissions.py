from rest_framework import permissions, viewsets

from django.db import models
from django.http import HttpRequest, HttpResponse


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(
        self: permissions,
        request: HttpRequest,
        view: viewsets.ModelViewSet,
        obj: models.Model,
    ) -> HttpResponse:
        del view
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsModerator(permissions.BasePermission):
    ...


class IsAdmin(permissions.BasePermission):
    ...


class IsSuperuser(permissions.BasePermission):
    ...
