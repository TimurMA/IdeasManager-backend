from rest_framework.serializers import ModelSerializer

from .models import Idea

class IdeaSerializer(ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'
        extra_kwargs = {
            'time_create': {'read_only': True},
            'time_update': {'read_only': True}
        }
        