from django.urls import path, include


urlpatterns = [
    path('api/estate/', include('estate.urls')),
    # path('api/user/', include('users.urls')),
    path('api/locales/', include('locales.urls')),

    # ---Admin urls
    path('api/admin/estate/', include('estate.urlsAdmin')),
    path('api/admin/user/', include('users.urlsAdmin')),
    path('api/admin/locales/', include('locales.urlsAdmin')),

]
