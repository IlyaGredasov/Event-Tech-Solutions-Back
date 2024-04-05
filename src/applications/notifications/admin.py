from applications.api.admin import register_app_models
from applications.notifications.apps import NotificationsConfig

register_app_models(app_name=NotificationsConfig.name)
