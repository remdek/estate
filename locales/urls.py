from django.urls import path

from .views import *

app_name = 'locales'

#/api/locales/

urlpatterns = [
     path('location/', LocationView.as_view(), name='location-view'),
     # path('top-menu-links/', topMenuLinksView.as_view(), name='topMenuLinks-view'),
]