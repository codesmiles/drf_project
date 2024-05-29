from django.urls import path
from . import views


urlpatterns = [
    path('', views.CommentListCreateView.as_view(), name="comments"), # create a new comment and view all comments created with POST and GET requests
    path("<int:comment_id>", views.CommentsRetrieveUpdateAndDeleteView.as_view(), name="comment"),
    path("update/<int:comment_id>", views.CommentsRetrieveUpdateAndDeleteView.as_view(), name="comment_update"),
    path("delete/<int:comment_id>", views.CommentsRetrieveUpdateAndDeleteView.as_view(), name="comment_delete"),
    
]