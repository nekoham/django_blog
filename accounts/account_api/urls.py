from accounts.account_api import views
from django.urls import path

app_name="account_api"
urlpatterns = [
    path('accounts/list/', views.UserListData.as_view(), name='userlistdata'),
    path('accounts/<int:pk>/', views.UserDetailData.as_view(), name='userdetaildata'),
    path('accounts/<int:pk>/delete/', views.UserDeleteData.as_view(), name='userdeletedata'),
    path('accounts/register/', views.UserCreateData.as_view(), name='userregisterdata'),
    path('accounts/login/',views.UserLoginData.as_view(), name='userlogindata'),
    path('accounts/<int:pk>/update/', views.UserUpdateData.as_view(), name='userupdatedata'),
    path('accounts/logout/', views.UserLogoutData.as_view(), name='userlogoutdata')
]
