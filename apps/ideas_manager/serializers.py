from rest_framework import serializers

from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'initator', 'problem', 'solution', 'proposed_result', 'name', 'time_create', 'time_update', 'status', 'rating', 'risk')