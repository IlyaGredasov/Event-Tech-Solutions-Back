from django.urls import include, path


urlpatterns = [
    path('users/', include('applications.users.api.urls')),
    path('events/', include('applications.events.api.urls')),
    path('auth/', include('applications.jwt_auth.api.urls')),
    path('notifications/', include('applications.notifications.api.urls'))
]
