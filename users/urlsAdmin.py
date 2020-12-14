from django.urls import path, include

from .viewsAdmin import *

app_name = 'usersAdmin'

# /api/admin/user/

urlpatterns = [
    path('', UserListAdminView.as_view(), name='userListAdminView'),
    path('<int:id>/', UserDetailAdminView.as_view(), name='userDetailAdminView'),
    path('group/', UserGroupListAdminView.as_view(), name='userGroupListAdminView'),
    path('auth/', include('djoser.urls')),
    path('token/', include('djoser.urls.authtoken'))
]
