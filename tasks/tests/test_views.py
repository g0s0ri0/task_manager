from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_task_list_requires_login(self):
        response = self.client.get(reverse('task-list'))
        self.assertNotEqual(response.status_code, 200)
    
    def test_task_list_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
