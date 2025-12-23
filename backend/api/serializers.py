"""Настройка сериализатора серверной части проекта."""


from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Класс сериализера Task."""

    class Meta:
        """Класс Meta для TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
