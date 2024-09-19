from applications.api.exceptions import PermissionDeniedException
from applications.api.permissions import is_manager, is_admin
from applications.events.models import Event
from applications.notifications.models import Notification
from applications.users.models import User


def create_notification(actor: User,
                        event: Event,
                        user: User,
                        description: str) -> Notification:
    if not is_manager(actor) and not is_admin(actor):
        raise PermissionDeniedException()
    return Notification.objects.create(
        event=event,
        user=user,
        description=description,
    )


def update_notification(notification: Notification,
                        actor: User,
                        **kwargs) -> Notification:
    if not is_manager(actor) and not is_admin(actor):
        raise PermissionDeniedException()
    notification.description = kwargs.get('description')
    notification.save()
    return notification
