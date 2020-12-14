from django.urls import path

from .views import *

app_name = 'estate'

#/api/estate/

urlpatterns = [
    path('category/tree/', EstateCategoryTreeView.as_view({'get': 'roots'}), name='EstateCategoryTreeView'),

]