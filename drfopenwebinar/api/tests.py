from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task

# Create your tests here.
class TaskAPITest(APITestCase):
    
    fixtures = ['task', 'user']
    
    def _authenticate(self):
        # my_user = User.objects.create_user('alejandro', password='contraseña1234')
        my_user = User.objects.get(username="alejandro", password="contraseña1234")

        token = Token.objects.create(user=my_user)
        self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + token.key)



    
    def test_get_tasks(self):
        # User.objects.create_user('alejandro', password='contraseña1234')
        #my_user = User.objects.create_user('alejandro', password='contraseña1234')
        
        #Task.objects.create(title=f'Tarea 1', description=f'Descripcion 1', complete=f'False')
        #Task.objects.create(title=f'Tarea 2', description=f'Descripcion 2', complete=f'True')
        
        # token = Token.objects.create(user=my_user)
        # self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + token.key)
        # self.client.login(username='alejandro', password='contraseña1234')
        
        self._authenticate()
        
        response = self.client.get('/api/tareas/')
        response_json = response.json()
        # print(response_json)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 2)
        self.assertIsInstance(response_json, list)
        self.assertIsInstance(response_json[0], dict)
        self.assertIsInstance(response_json[1], dict)
    
    def test_post_tasks(self):
        self._authenticate()
        url = '/api/tareas/'
        data = {'title':'Test Task', 'description':'Test Description', 'complete':False}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')
        
    
    

