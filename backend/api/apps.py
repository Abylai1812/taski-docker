"""Общая настройка серверной части проекта."""


from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Настройка класса ApiConfig."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
