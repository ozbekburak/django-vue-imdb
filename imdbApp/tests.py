from rest_framework.test import APITestCase, APIClient


class test_movie(APITestCase):
    def setUp(self):
        self.data={"title":"Oslo 31"}

    def test_worksAPIorNot(self):
        client = APIClient()
        response=client.post('movietitle/', {'title':'oslo 31'}, format='json')
        print(response.status_code)
        assert response.status_code==200