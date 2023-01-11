from django.db import models
from django.urls import (
    reverse,
)  # Nos permite referenciarnos al objeto por el nombre del template URL.

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)  # un titulo de no mas de 200 caracteres
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )  # cuando elimina algun padre elimina la herencia
    body = models.TextField(
        max_length=500
    )  # un recuadro de texto de no mas de 500 caracteres.

    def __str__(self):
        return self.title  # nos retorna el titulo en el admin de Django

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
