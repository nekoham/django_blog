from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("createblog/", views.CreateBlogView.as_view(), name="createblog"),
    path("updateblog/<int:pk>", views.UpdateBlogView.as_view(), name="updateblog"),
    path("deleteblog/<int:pk>", views.DeleteBlogView.as_view(), name="deleteblog"),
    path("createcomment/<int:blog_id>", views.CreateCommentView.as_view(), name="createcomment"),
    path("updatecomment/<int:pk>", views.UpdateCommentView.as_view(), name="updatecomment"),
    path("deletecomment/<int:pk>", views.DeleteCommentView.as_view(), name="deletecomment"),
]
