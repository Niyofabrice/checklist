from rest_framework import serializers
from .models import ChecklistItem

class ChecklistItemSerializer(serializers.ModelSerializer):
    sub_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ChecklistItem
        fields = ['id', 'user', 'title', 'description', 'completed', 'parent', 'sub_items', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
