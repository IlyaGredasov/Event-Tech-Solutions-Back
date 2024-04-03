from applications.api.admin import register_app_models
from applications.events.apps import EventsConfig


register_app_models(app_name=EventsConfig.name)
