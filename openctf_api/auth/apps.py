from django.apps import AppConfig

class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'
    label = 'authentication'

class AuthorizationConfig(AppConfig):
    name = 'django.contrib.auth'
    verbose_name = 'Authorization'
