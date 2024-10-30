from rest_framework.permissions import BasePermission

class CanImmobilizeVehicle(BasePermission):
    """
    Custom permission to only allow authorized users to immobilize vehicles.
    """
    def has_permission(self, request, view):
        # Replace 'fleet_manager' with your actual user role for immobilization access
        return request.user.is_authenticated and request.user.role == 'fleet_manager'
