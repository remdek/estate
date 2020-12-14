from django.urls import path

from .viewsAdmin import *

app_name = 'estateAdmin'

#/api/admin/estate/

urlpatterns = [
    path('', EstateListAdminView.as_view(), name='estateListAdminView'),
    path('<int:id>/', EstateDetailAdminView.as_view(), name='estateDetailAdminView'),
    path('category/', CategoryListAdminView.as_view(), name='categoryListAdminView'),
    path('category/<int:id>/', CategoryDetailAdminView.as_view(), name='categoryDetailAdminView'),
    path('category/props/', EstatePropsListAdminView.as_view(), name='estatePropsListAdminView'),
    path('category/props/opts/', EstatePropOptionsListAdminView.as_view(), name='estatePropOptionsListAdminView'),

]