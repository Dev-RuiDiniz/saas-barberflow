def tenant_filter(queryset, tenant):
    """Filtra automaticamente por tenant_id."""
    return queryset.filter(tenant=tenant)
