from django.apps import AppConfig


class AuthAbstractBaseUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_abstract_base_user'
