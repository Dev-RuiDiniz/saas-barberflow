from rest_framework import serializers
from .models import Scheduling


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = "__all__"
        read_only_fields = ["tenant"]
