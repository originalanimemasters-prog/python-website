from rest_framework.permissions import BasePermission


class IsPremiumUser(BasePermission):
    """
    Temporary implementation.
    Later this will check the user's active premium subscription.
    """

    message = "A premium subscription is required to access this resource."

    def has_permission(self, request, view):
        return request.user.is_authenticated