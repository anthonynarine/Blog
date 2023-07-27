from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import testcases

from .models import Post

class BlogTests(TestCase):
    """
    The BlogTests class contains unit tests for the Post model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        setUpTestData is called once at the beginning of the test run for class-level setup.
        """
        cls.user = get_user_model().objects.create_user(
            username = "batman", 
            email = "test@email.com",
            password = "batcave",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "batman begins",
            body = "why so serious"
        )
    
    def test_post_model(self):
        """
        test_post_model checks if the created Post instance has the correct attributes.
        """
        self.assertEqual(self.post.author.username, "batman")
        self.assertEqual(self.post.title, "batman begins")
        self.assertEqual(self.post.body, "why so serious")
        self.assertEquals(str(self.post), "batman begins")



        


