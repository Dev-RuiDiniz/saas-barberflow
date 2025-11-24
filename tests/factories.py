import factory
from tenants.models import Establishment
from apps.clients.models import Client
from apps.services.models import Service
from apps.employees.models import Employee
from apps.scheduling.models import Scheduling


class TenantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Establishment

    name = "Barbearia XPTO"
    subdomain = factory.Faker("slug")
    cnpj = "12345678910"


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    tenant = factory.SubFactory(TenantFactory)
    name = factory.Faker("name")
    email = factory.Faker("email")


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    tenant = factory.SubFactory(TenantFactory)
    name = factory.Faker("name")
    role = "Barbeiro"


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    tenant = factory.SubFactory(TenantFactory)
    name = "Corte"
    duration = 30
    price = 50.00


class SchedulingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Scheduling

    tenant = factory.SubFactory(TenantFactory)
    client = factory.SubFactory(ClientFactory)
    employee = factory.SubFactory(EmployeeFactory)
    service = factory.SubFactory(ServiceFactory)
    datetime = "2025-01-01T08:00:00Z"
