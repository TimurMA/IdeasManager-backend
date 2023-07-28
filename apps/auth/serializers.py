from rest_framework.serializers import ModelSerializer
from .models import User, Role

from django.contrib.auth.hashers import make_password
from bcrypt import gensalt

import uuid

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('user', 'role')

class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email', 'is_registered')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_registered': {'write_only': True},
        }

    def to_internal_value(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        roles = data.get('roles')
        data.update({
                'token': str(uuid.uuid4()),
                'is_registered': True,
                'first_name': first_name if first_name else 'Джон',
                'last_name': last_name if last_name else 'Доу',
                'password': make_password(password, gensalt()),
                })
        return super(UserAuthSerializer, self).to_internal_value(data)
    
class UserInvitationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'token')

    def to_internal_value(self, data):
        data.update({
                'token': str(uuid.uuid4())
                })
        return super(UserInvitationSerializer, self).to_internal_value(data)