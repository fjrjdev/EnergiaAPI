from django.utils.translation import gettext as _
from rest_framework import serializers
from .services.cep_service import cep_service

def validate_cep(cep):
    data = cep_service(cep)
    error = data.get("erro", None)

    if data and not error:
        return data
    message = _("Invalid CEP")
    raise serializers.ValidationError(message)