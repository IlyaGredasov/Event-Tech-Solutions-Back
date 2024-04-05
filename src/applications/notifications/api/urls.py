from rest_framework.routers import SimpleRouter

from applications.notifications.api import views

router = SimpleRouter()
router.register(r'notification', views.NotificationViewSet)

urlpatterns = router.urls
