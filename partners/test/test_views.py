from rest_framework.test import APITestCase

from partners.models import Partner
from .mocks import mock_partner, mock_partner_two, mock_partner_login, mock_partner_two_login

class PartnerViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.base_URL = "/partners/"
        self.login = "/login/"
        
        self.partner_data = mock_partner
        self.partner_data_two = mock_partner_two
        self.partner_data_login = mock_partner_login
        self.partner_two_data_login = mock_partner_two_login

    def test_can_create_partner(self):
        response = self.client.post(self.base_URL, self.partner_data_two, format="json")

        self.assertEqual(response.status_code, 201)

    def test_can_create_partner_with_same_name(self):
        self.client.post(self.base_URL, self.partner_data_two, format="json")
        response = self.client.post(self.base_URL, self.partner_data_two, format="json")

        self.assertEqual(response.status_code, 400)

    def test_can_partner_update_by_id(self):
        data = {"cnpj": "87244882000109"}
        partner = self.client.post(self.base_URL, self.partner_data, format="json")
        partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + partner_access.data["access"])

        response = self.client.patch(
            f"{self.base_URL}{partner.data['id']}/", data, format="json"
        )

        data = {**response.data, "cnpj":data["cnpj"]}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)

    def test_cant_update_user_without_authentication(self):
        data = {"cnpj": "87244882000109"}
        partner = self.client.post(self.base_URL, self.partner_data, format="json")

        response = self.client.patch(
            f"{self.base_URL}{partner.data['id']}/", data, format="json"
        )

        message = {"detail": "Authentication credentials were not provided."}

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, message)

    def test_can_delete_user_with_same_id(self):
        partner = self.client.post(self.base_URL, self.partner_data, format="json")
        partner_access = self.client.post(self.login, self.partner_data_login, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + partner_access.data["access"])

        response = self.client.delete(
            f"{self.base_URL}{partner.data['id']}/", None, format="json"
        )

        self.assertEqual(response.status_code, 204)

    def test_can_list_last_partners(self):
        partner = self.client.post(self.base_URL, self.partner_data, format="json")
        partner_two = self.client.post(self.base_URL, self.partner_data_two, format="json")
        response = self.client.get(self.base_URL + "last-partners/", format="json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)