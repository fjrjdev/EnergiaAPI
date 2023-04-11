from rest_framework import serializers

from django.core.validators import MinLengthValidator

from .models import Plant
from partners.serializers import PartnerSerializer
from .validators import validate_cep

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

    def validate(self, data):
        if data["cep"]:
            validate_cep(data['cep'])
        return data

class PlantDetailSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True)
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
    
    def validate(self, data):
        cep = data.get("cep", None)
        if cep:
            validate_cep(data['cep'])
        return data