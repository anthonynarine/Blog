from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import testcases

from .models import Post

# command python3 manage.py test

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        self.assertEqual(self.post.author.username, "batman")
        self.assertEqual(self.post.title, "batman begins")
        self.assertEqual(self.post.body, "why so serious")
        self.assertEquals(str(self.post), "batman begins")



        


