from django.test import TestCase
from django.contrib.auth import get_user_model
from .views import Post
from django.urls import reverse

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

    def test_url_exist_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_detailview(self):
        response = self.client.get("/post/1")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get("home")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Titulo")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_createview(self):
        response = self.client.get(
            reverse("post_new"),
            {"title": "titulo nuevo", "body": "body nuevo", "author": self.user.id},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "titulo nuevo")
        self.assertEqual(Post.objects.last().body, "body nuevo")
        """Post.objects.last() nos muestra el ultimo objeto creado en nuestro modelo."""

    def test_post_updateview(self):
        response = self.client.get(
            reverse("post_edit", args="1"),
            {"title": "titulo actualizado", "body": "body actualizado"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "titulo actualizado")
        self.assertEqual(Post.objects.last().body, "body actualizado")

    def test_post_deleteview(self):
        response = self.client.get("post_delete", args="1")
        self.assertEqual(response.status_code, 302)
