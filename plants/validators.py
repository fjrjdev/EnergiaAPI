from django.utils.translation import gettext as _
from rest_framework import serializers
from services.cep_service import cep_service

def validate_cep(cep):
    data = cep_service(cep)
    if data:
        return data
    message = _("Invalid CEP")
    raise serializers.ValidationError(message)