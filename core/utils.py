# Funções utilitárias globais do projeto
def get_tenant_from_request(request):
    """
    Retorna o tenant atual identificado pelo middleware.
    """
    return getattr(request, "tenant", None)
