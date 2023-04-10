from django.db import models
import uuid


class Plant(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    name = models.CharField(max_length=200, unique=True, error_messages={"unique": "A plant with that name already exists."})
    cep = models.CharField(unique=True, error_messages={"unique": "A plant with that cep already exists."})

    latitude = models.FloatField()
    longitude = models.FloatField()
    maximum_capacity_GW = models.IntegerField()

    partner = models.ForeignKey(
        'partners.Partner',
        on_delete=models.CASCADE,
        related_name="partner"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

