from rest_framework.routers import SimpleRouter

from rest_framework_nested.routers import NestedSimpleRouter

from applications.users.api.views import UserViewSet, UserAchievementViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet)

user_router = NestedSimpleRouter(router, r'user', lookup='user')
user_router.register(r'event', UserAchievementViewSet)
urlpatterns = router.urls + user_router.urls
