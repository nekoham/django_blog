from accounts.api import views
from django.urls import path

urlpatterns = [
    path('list/', views.UserListData.as_view(), name='userlistdata'),
    path('<int:pk>/', views.UserDetailData.as_view(), name='userdetaildata'),
    path('<int:pk>/delete/', views.UserDeleteData.as_view(), name='userdeletedata'),
    path('register/', views.UserCreateData.as_view(), name='userregisterdata'),
    path('login/',views.UserLoginData.as_view(), name='userlogindata'),
    path('<int:pk>/update/', views.UserUpdateData.as_view(), name='userupdatedata'),
    path('logout/', views.UserLogoutData.as_view(), name='userlogoutdata')
]
