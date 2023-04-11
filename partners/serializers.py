import re

from rest_framework import serializers
from .models import Partner
from .validators import cnpj_validator

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            "id",
            "name",
            "cnpj",
            "email",
            "password",
            "created_at", 
            "updated_at"]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]
        extra_kwargs= {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs['cnpj']:
            cnpj_validator(attrs['cnpj'])
            attrs['cnpj'] = re.sub("[^0-9]", "", attrs['cnpj'])
        return attrs

    def create(self, validated_data):
        user = Partner(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user