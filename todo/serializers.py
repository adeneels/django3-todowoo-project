from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important', 'user']
