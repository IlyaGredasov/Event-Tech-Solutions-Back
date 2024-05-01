from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from system import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('applications.api.urls')),
]

urlpatterns += (
        [
            path('schema/', SpectacularAPIView.as_view(), name='schema'),
            path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
