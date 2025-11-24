def create_establishment_detail(tenant, validated_data):
    return tenant.establishmentdetail_set.create(**validated_data)
