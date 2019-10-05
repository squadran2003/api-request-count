from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import ApiRequest

"""before running the tests please add the apiRequestCount url to the global apps urls"""


class TestApiRequestCountApp(TestCase):
    def setUp(self):
        User.objects.create(
            username='andy',
            password='innocent23'
        )
        self.user = User.objects.get(username='andy')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_view_request_count(self):
        # will make 10 request which should nave 
        # 10 records in the ApiRequest table with the current user
        # and the view name test view
        for i in range(10):
            response = self.client.get('/api/v1/apirequestcount/1/', format='json')
            response2 = self.client.get('/api/v1/apirequestcount/2/', format='json')
            self.assertEqual(200, response.status_code)
            self.assertEqual(200, response2.status_code)
        # test that the view1 save  are 10 rows in ApiRequest Table
        query1 = ApiRequest.objects.filter(user=self.user,view_name="test view1")
        self.assertEqual(10,len(query1))
        # test that the view2 save  are 10 rows in ApiRequest Table
        query2 = ApiRequest.objects.filter(user=self.user,view_name="test view2")
        self.assertEqual(10,len(query2))

