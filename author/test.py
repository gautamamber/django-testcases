from django.test import  TestCase, Client
from .models import User
from .forms import RegistrationForm
from django.urls import reverse

class UserTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create(
            username = "gautam",
            email = "amber@nickelfox.com",
            user_type = User.AUTHOR
        )
        self.publisher = User.objects.create(
            username = "Mark",
            email = "amber+1@nickelfox.com",
            user_type = User.PUBLISHER,
            no_of_books = 12
        )
    def test_get_publisher(self):
        self.assertEquals(User.PUBLISHER, 2)
    
    def test_get_author(self):
        self.assertEqual(User.AUTHOR, 1)
    
    def test_can_write(self):
        self.assertTrue(self.author.can_write_books())
    
    def test_can_write_2(self):
        self.assertFalse(self.publisher.can_write_books())
    
class TestRegistrationForm(TestCase):

    def test_registration_form(self):
        invalid_data = {
                "username" : "amber gautam",
                "password" : "Amber1998@",
                "confirm" : "Amber"
        }

        form = RegistrationForm(data = invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)
    
        valid_data = {
                "username" : "amber gautam",
                "password" : "Amber1998@",
                "confirm" : "Amber1998@"
        }

        form = RegistrationForm(data = valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
    
class TestUserRegistrationView(TestCase):
    
    def setUp(self):
        self.client = Client()

        def test_registration(self):
            url = reverse('register')

            response = self.client.get(url)
            self.assertEqual(response.status, 200)

            response = self.client.post(url, {})
            self.assertEqual(response.status, 200)

            exp_data = {
            'error': True,
            'errors': {
                'username': 'This field is required',
                'password': 'This field is required',
                'confirm': 'This field is required',
            }
            }
            self.assertEqual(exp_data, response.json())

            req_data = {
                'username': 'user@test.com',
                'password': 'secret',
                'confirm': 'secret1',
            }
            response = self.client.post(url, req_data)
            self.assertEqual(response.status, 200)
            exp_data = {
                'error': True,
                'errors': {
                    'confirm': 'Passwords mismatched'
                }
            }
            self.assertEqual(exp_data, response.json())

            req_data = {
                'username': 'user@test.com',
                'password': 'secret',
                'confirm': 'secret',
            }
            response = self.client.post(url, req_data)
            self.assertEqual(response.status, 200)
            exp_data = {
                'error': False,
                'message': 'Success, Please login'
            }
            self.assertEqual(exp_data, response.json())
            self.assertEqual(User.objects.count(), 1)
