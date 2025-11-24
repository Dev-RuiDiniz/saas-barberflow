from rest_framework.permissions import BasePermission

class IsTenantObject(BasePermission):
    """
    Garante que o usuário só acesse objetos do seu tenant.
    """

    def has_object_permission(self, request, view, obj):
        tenant = getattr(request, "tenant", None)
        return tenant and obj.establishment_id == tenant.id
