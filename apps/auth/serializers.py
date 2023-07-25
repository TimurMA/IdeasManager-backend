from rest_framework.serializers import ModelSerializer
from .models import User


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'pk': {'read_only': True},
            'password': {'write_only': True}
        }
