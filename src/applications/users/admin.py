from applications.api.admin import register_app_models
from applications.users.apps import UsersConfig


register_app_models(UsersConfig.name)
