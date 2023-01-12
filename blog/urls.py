from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path(
        "post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"
    ),  # PK es la primary key, es el id que agrega django a la base de datos.
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
]
