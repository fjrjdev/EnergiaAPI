from django.test import TestCase
from uuid import uuid4

from partners.models import Partner
from partners.test.mocks import mock_partner
from plants.models import Plant

from .mocks import mock_plant

class PlantModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.plant_data = mock_plant
        
        self.partner = Partner.objects.create(**mock_partner)
        self.plant = Plant.objects.create(
            **self.plant_data,
        partner=self.partner
        )

    def test_fields(self):
        plant = Plant.objects.get(id=self.plant.id)
        
        id = plant._meta.get_field("id")
        name = plant._meta.get_field("name")
        cep = plant._meta.get_field("cep")
        latitude = plant._meta.get_field("latitude").get_internal_type()
        longitude = plant._meta.get_field("longitude").get_internal_type()
        maximum_capacity_GW = plant._meta.get_field("maximum_capacity_GW").get_internal_type()
        
        self.assertIsInstance(plant, Plant)
        self.assertEqual(plant, self.plant)

        self.assertIsNotNone(id)
        self.assertEqual(id.default, uuid4)
        self.assertTrue(id.primary_key)
        self.assertFalse(id.editable)
        
        self.assertTrue(name.unique)
        self.assertEqual(name.max_length, 200)
        
        self.assertTrue(cep.unique)
        self.assertEqual(cep.error_messages['unique'], "A plant with that cep already exists.")

        self.assertEqual(latitude, 'FloatField')
        self.assertEqual(longitude, 'FloatField')
        self.assertEqual(maximum_capacity_GW, 'PositiveSmallIntegerField')

    def test_plant_relations(self):
        self.assertEqual(
            self.plant.partner_id,
            self.partner.id
        )
