from django.test import  TestCase
from .models import User
from .forms import RegistrationForm

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

