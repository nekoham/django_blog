from accounts import views
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path('', views.UserList.as_view(), name='userlist'),
    path('<int:pk>/', views.UserDetail.as_view(), name='userdetail'),
    path('register/', views.UserRegister.as_view(), name='userregister'),
    path('login/', views.UserLogin.as_view(), name='userlogin'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='userdelete'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='userdelete'),
]
