from rest_framework import generics
from core.permissions import IsTenantUser
from .models import EstablishmentDetail
from .serializers import EstablishmentDetailSerializer


class EstablishmentDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = EstablishmentDetailSerializer
    permission_classes = [IsTenantUser]

    def get_object(self):
        return EstablishmentDetail.objects.get(tenant=self.request.tenant)
