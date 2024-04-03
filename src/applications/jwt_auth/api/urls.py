from django.urls import re_path

from applications.jwt_auth.api import views


urlpatterns = [
    re_path(r'^login/$', views.CustomLoginView.as_view(), name='login'),
    re_path(r'^user/$', views.CustomUserDetailsView.as_view(), name='user'),
]
