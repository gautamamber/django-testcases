from django.test import  TestCase
from .models import User

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
            user_type = User.PUBLISHER
        )
    def test_get_publisher(self):
        self.assertEquals(User.PUBLISHER, 2)
    
    def test_get_author(self):
        self.assertEqual(User.AUTHOR, 1)