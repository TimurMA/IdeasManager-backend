from rest_framework.serializers import ModelSerializer
from .models import User

from django.contrib.auth.hashers import make_password
from bcrypt import gensalt

import uuid

class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def to_internal_value(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        data.update(
            {
                'token': uuid.uuid4(),
                'first_name': first_name if first_name else 'Джон',
                'last_name': last_name if last_name else 'Доу',
                'password': make_password(password, gensalt())
            }
        )
        return super(UserAuthSerializer, self).to_internal_value(data)