



from rest_framework import permissions

class IsDispatcherOrAdminOrFleetManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only users with dispatcher, admin, or fleet manager roles
        return request.user and (
            request.user.is_staff or  # admin
            request.user.role in ['dispatcher', 'fleet_manager']  # custom roles
        )

    def has_object_permission(self, request, view, obj):
        # Ensure only assigned dispatchers and admins can modify trips
        return self.has_permission(request, view)






from rest_framework.permissions import BasePermission

class IsDispatcherOrAdmin(BasePermission):
    """
    Allows access only to dispatchers and admins.
    """
    def has_permission(self, request, view):
        return request.user and (request.user.is_admin or request.user.is_dispatcher)

class CanAssignToFleetManager(BasePermission):
    """
    Allows admins to assign trips to fleet managers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_admin





from rest_framework.permissions import BasePermission

class CanImmobilizeVehicle(BasePermission):
    """
    Custom permission to only allow authorized users to immobilize vehicles.
    """
    def has_permission(self, request, view):
        # Replace 'fleet_manager' with your actual user role for immobilization access
        return request.user.is_authenticated and request.user.role == 'fleet_manager'
