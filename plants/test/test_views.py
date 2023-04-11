from rest_framework.test import APITestCase

from partners.test.mocks import mock_partner, mock_partner_login, mock_partner_two
from partners.models import Partner
from plants.models import Plant
from plants.serializers import PlantSerializer
from .mocks import mock_plant

class PlantViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.base_URL = "/plants/"
        self.login = "/login/"
        self.partner_data = mock_partner
        self.partner_data_login = mock_partner_login
        self.partner_instance = Partner.objects.create(**mock_partner_two)
        self.plant_data = mock_plant

    def test_can_create_plant(self):
        self.partner = self.client.post("/partners/", self.partner_data, format="json")
        self.partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.access = self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.partner_access.data["access"]) 
        
        response = self.client.post(self.base_URL, self.plant_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Plant.objects.count(), 1)
        self.assertEqual(str(response.data["partner_id"]), self.partner.data['id'])

    def test_cant_create_plant_with_same_name(self):
        self.partner = self.client.post("/partners/", self.partner_data, format="json")
        self.partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.access = self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.partner_access.data["access"])

        self.client.post(self.base_URL, self.plant_data, format="json")
        response = self.client.post(self.base_URL, self.plant_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_can_plant_update_by_id(self):
        self.partner = self.client.post("/partners/", self.partner_data, format="json")
        self.partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.access = self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.partner_access.data["access"]) 
        data = {	
            "cep": "68550370"
        }

        plant = self.client.post(self.base_URL, self.plant_data, format="json")
        response = self.client.patch(
            f"{self.base_URL}{plant.data['id']}/", data, format="json"
        )

        data = {**response.data, "cep":data["cep"]}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)

    def test_cant_update_plant_without_authentication(self):
        data = {"cnpj": "87244882000109"}
        self.plant = Plant.objects.create(
            name="Test Plant",
            cep="12345678",
            latitude=0.0,
            longitude=0.0,
            maximum_capacity_GW=100,
            partner_id=self.partner_instance.id
        )
        
        response = self.client.patch(
            f"{self.base_URL}{self.plant.id}/", data, format="json"
        )

        message = {"detail": "Authentication credentials were not provided."}

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, message)

    def test_can_delete_user_with_same_id(self):
        self.partner = self.client.post("/partners/", self.partner_data, format="json")
        self.partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.access = self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.partner_access.data["access"]) 
        self.plant = Plant.objects.create(
            name="Test Plant",
            cep="12345678",
            latitude=0.0,
            longitude=0.0,
            maximum_capacity_GW=100,
            partner_id=self.partner.data["id"]
        )
        
        response = self.client.delete(
            f"{self.base_URL}{self.plant.id}/", None, format="json"
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Plant.objects.count(), 0)

    def test_can_list_top_capacity_plants(self):
        self.plant = Plant.objects.create(
            name="Test Plant",
            cep="987654321",
            latitude=0.0,
            longitude=0.0,
            maximum_capacity_GW=100,
            partner_id=self.partner_instance.id
        )
        self.plant2 = Plant.objects.create(
            name="Test Plant 2",
            cep="12345678",
            latitude=0.0,
            longitude=0.0,
            maximum_capacity_GW=1000,
            partner_id=self.partner_instance.id
        )
        response = self.client.get(self.base_URL + "top-capacity/", format="json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        expected_data = PlantSerializer(
            [self.plant2, self.plant],
            many=True
        ).data
        self.assertEqual(response.data, expected_data)