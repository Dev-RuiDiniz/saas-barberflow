from rest_framework import serializers
from .models import EstablishmentDetail


class EstablishmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstablishmentDetail
        fields = "__all__"
        read_only_fields = ["tenant"]
