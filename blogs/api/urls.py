from blogs.api import views
from django.urls import path

urlpatterns = [
    path('blogs/list/', views.IndexData.as_view(), name='bloglistdata'),
    path('blogs/<int:pk>/', views.DetailData.as_view(), name='blogdetaildata'),
    path('blogs/<int:pk>/delete/', views.DeleteBlogData.as_view(), name='blogdeletedata'),
    path('blogs/create/', views.CreateBlogData.as_view(), name='blogcreatedata'),
    path('blogs/<int:pk>/update/', views.UpdateBlogData.as_view(), name='blogupdatedata'),
    path('comments/<int:blog_id>/list/', views.ListCommentData.as_view(), name='commentlistdata'),
    path('comments/<int:pk>/', views.DetailCommentData.as_view(), name='commentdetaildata'),
    path('comments/<int:pk>/delete/', views.DeleteCommentData.as_view(), name='commentdeletedata'),
    path('comments/<int:blog_id>/create/', views.CreateCommentData.as_view(), name='commentcreatedata'),
    path('comments/<int:pk>/update/', views.UpdateCommentData.as_view(), name='commentupdatedata'),
    path('tags/list/', views.ListTagData.as_view(), name='taglistdata'),
]
