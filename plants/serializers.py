from rest_framework import serializers
from .models import Plant
from partners.serializers import PartnerSerializer

class PlantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Plant
        fields = [
            "id",
            "name",
            "cep",
            "latitude",
            "longitude",
            "maximum_capacity_GW",
            "partner_id",
            "created_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]

class PlantDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Plant
        fields = [
            "id",
            "name",
            "cep",
            "latitude",
            "longitude",
            "maximum_capacity_GW",
            "created_at",
            "updated_at",
            "partner"
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]
        depth = 1
    partner = PartnerSerializer(read_only=True)