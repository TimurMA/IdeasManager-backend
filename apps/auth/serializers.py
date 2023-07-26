from rest_framework.serializers import ModelSerializer
from .models import User


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'first_name', 'last_name', 'role', 'is_superuser')
        extra_kwargs = {
            'pk': {'read_only': True},
            'password': {'write_only': True},
            'is_superuser': {'write_only': True}
        }

    def to_internal_value(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        role = data.get('role')
        data.update({
                'first_name': first_name if first_name else 'Джон',
                'last_name': last_name if last_name else 'Доу',
                'is_superuser': True if role=='Admin' else False
                })
        return super(UserAuthSerializer, self).to_internal_value(data)