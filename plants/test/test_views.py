from rest_framework.test import APITestCase

from partners.test.mocks import mock_partner, mock_partner_login
from partners.models import Partner
from plants.models import Plant
from .mocks import mock_plant

class PlantViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.base_URL = "/plants/"
        self.login = "/login/"
        self.partner_data = mock_partner
        self.partner_data_login = mock_partner_login

        self.plant_data = mock_plant

    def test_can_create_plant(self):
        self.partner = self.client.post("/partners/", self.partner_data, format="json")
        self.partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.access = self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.partner_access.data["access"]) 
        
        response = self.client.post(self.base_URL, self.plant_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(str(response.data["partner_id"]), self.partner.data['id'])

    def test_cant_create_plant_name(self):
        self.partner = self.client.post("/partners/", self.partner_data, format="json")
        self.partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.access = self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.partner_access.data["access"])

        self.client.post(self.base_URL, self.plant_data, format="json")
        response = self.client.post(self.base_URL, self.plant_data, format="json")
        self.assertEqual(response.status_code, 400)