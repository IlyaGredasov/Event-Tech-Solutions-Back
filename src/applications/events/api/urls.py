from rest_framework.routers import SimpleRouter

from rest_framework_nested.routers import NestedSimpleRouter

from applications.events.api import views


router = SimpleRouter()
router.register(r'event', views.EventViewSet)


events_router = NestedSimpleRouter(router, r'event', lookup='event')
events_router.register(r'participants', views.EventParticipantViewSet, basename='event-participants')


urlpatterns = router.urls + events_router.urls
