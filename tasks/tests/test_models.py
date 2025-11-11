from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_create_task(self):
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            status='pending'
        )
        self.assertEqual(str(task), 'Test Task')
        self.assertEqual(task.status, 'pending')
    
    def test_task_default_status(self):
        task = Task.objects.create(
            user=self.user,
            title='Test Task'
        )
        self.assertEqual(task.status, 'pending')
