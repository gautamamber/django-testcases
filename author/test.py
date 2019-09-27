from django.test import  TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create(
            username = "gautam",
            email = "amber@nickelfox.com",
            user_type = User.AUTHOR
        )
        self.author = User.objects.create(
            username = "Mark",
            email = "amber+1@nickelfox.com",
            user_type = User.AUTHOR
        )
    def test_get_authors(self):
        self.assertEquals(User.get_authors(), 1)

    def test_can_write_books(self):
        self.assertTrue(self.author.can_write_books())
        self.assertFalse(self.publisher.can_write_books())