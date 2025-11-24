from tenants.models import Establishment
from django.http import JsonResponse

class TenantMiddleware:
    """
    Middleware simples para identificar o tenant via subdomínio.
    Exemplo: rui.saas-barberflow.com -> tenant = rui
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        host = request.get_host().split(":")[0]
        parts = host.split(".")

        if len(parts) > 2:  # subdomínio
            subdomain = parts[0]

            try:
                tenant = Establishment.objects.get(subdomain=subdomain)
                request.tenant = tenant
            except Establishment.DoesNotExist:
                return JsonResponse({"error": "Invalid tenant"}, status=404)
        else:
            request.tenant = None  # acesso sem tenant (API pública)

        return self.get_response(request)
