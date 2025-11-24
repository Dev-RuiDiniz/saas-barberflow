from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API interna
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/establishments/", include("apps.establishments.urls")),
    path("api/employees/", include("apps.employees.urls")),
    path("api/services/", include("apps.services.urls")),
    path("api/clients/", include("apps.clients.urls")),
    path("api/scheduling/", include("apps.scheduling.urls")),

    # API pública
    path("public/", include("public_api.urls")),
]

