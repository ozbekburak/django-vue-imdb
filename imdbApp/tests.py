import json
from rest_framework.test import APITestCase, APIClient


class test_movie(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data={"title":"Oslo 31"}
        self.response = self.client.post('movietitle/', {'title': 'oslo 31'}, format='json')

    def test_worksAPIorNot(self):
        print(self.response.status_code)
        assert self.response.status_code==200

    def test_movieTitle(self):
        self.assertTrue("Oslo, August 31st" in json.loads(self.response.content))