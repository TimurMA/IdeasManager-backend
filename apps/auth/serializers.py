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

    def to_internal_value(self, data):
        if not data.get('first_name'):
            data.update({'first_name': 'Джон'})
        if not data.get('last_name'):
            data.update({'last_name': 'Доу'})
        return super(UserAuthSerializer, self).to_internal_value(data)