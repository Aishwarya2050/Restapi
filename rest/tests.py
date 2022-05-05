from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from .models import Info

class InfoCreateTestCase(APITestCase):
    def test_create_info(self):
        self.rest_url = Info('rest')
        
        self.data={
            'checked' : 'checked',
            'name': 'name',
            'Type' : 'Type',
            'Age' : 'Age',
            'Description' : 'Description',
            'date' : 'date',
            
            
        }
        
        return super().test()
    
    def tearDown(self):
        return super().tearDown()