import requests

from django.utils.translation import gettext as _
from rest_framework import serializers

def validate_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    
    message = _("Invalid CEP")
    raise serializers.ValidationError(message)