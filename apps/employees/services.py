from .models import Employee  

def create_employee(tenant, validated_data):
    return Employee.objects.create(tenant=tenant, **validated_data)
