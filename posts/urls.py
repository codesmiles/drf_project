from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="posts_home"),
    path('post_lists', views.list_or_create_posts, name="post_lists"),
    path("post_lists/<int:post_id>/", views.get_single_post, name="post_details"),
    path("update/<int:post_id>/", views.update_post, name="post_update"),
    path("delete/<int:post_id>/", views.delete_post, name="post_delete"),
]
