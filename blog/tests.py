from django.test import TestCase
from django.contrib.auth import get_user_model
from .views import Post

# Create your tests here.


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="Titulo",
            body="Nice body",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Titulo")
        self.assertEqual(self.post.body, "Nice body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Titulo")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
