from django.test import TestCase
from uuid import uuid4

from partners.models import Partner

from .mocks import mock_partner, mock_partner_two

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.partner_data = mock_partner

        cls.partner = Partner.objects.create(**cls.partner_data)
    
    def test_partner_model(self):
        partner = Partner.objects.get(id=self.partner.id)

        id = partner._meta.get_field("id")
        name = partner._meta.get_field("name")
        email = partner._meta.get_field("email")
        cnpj = partner._meta.get_field("cnpj")

        self.assertIsInstance(partner, Partner)
        self.assertEqual(partner, self.partner)

        self.assertIsNotNone(id)
        self.assertEqual(id.default, uuid4)
        self.assertTrue(id.primary_key)
        self.assertFalse(id.editable)

        self.assertTrue(name.unique)
        self.assertTrue(name.max_length, 200)

        self.assertTrue(email.unique)
        self.assertTrue(email.max_length, 254)

        self.assertTrue(cnpj.unique)
        self.assertEqual(cnpj.error_messages["unique"], "A user with that cpnj already exists.")