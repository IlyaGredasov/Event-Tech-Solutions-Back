from rest_framework.routers import SimpleRouter

from applications.users.api.views import UserViewSet


router = SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns = router.urls
