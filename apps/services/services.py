def create_service(tenant, validated_data):
    return Service.objects.create(tenant=tenant, **validated_data)
