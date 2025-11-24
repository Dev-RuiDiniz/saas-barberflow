from tenants.models import Establishment
from django.http import Http404

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_id = request.headers.get("X-Tenant-ID")

        if not tenant_id:
            raise Http404("Tenant não informado")

        try:
            request.tenant = Establishment.objects.get(id=tenant_id)
        except Establishment.DoesNotExist:
            raise Http404("Tenant inválido")

        return self.get_response(request)
