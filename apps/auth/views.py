from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserAuthSerializer, RoleSerializer, UserInvitationSerializer
from .models import User, Role

from django.contrib.auth.hashers import check_password
from django.conf import settings

class LoginAPI(APIView):
    def post(self, request):
        try:
            user = User.objects.get(
                username=request.data["username"]
            )
            is_correct_password = check_password(
                request.data["password"], user.password
            )

            if is_correct_password:
                return Response({"user": UserAuthSerializer(user).data})
            else:
                return Response({"error": "Ошибка авторизации"})

        except:
            return Response({"error": "Ошибка авторизации"})



class InvitationRegisterAPI(APIView):
    def get(self, request, *args, **kwargs):
        token = kwargs.get('token', None)
        if not token:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            instance = User.objects.get(token=token)
        except:
            return Response({'error': 'Object does not exist'})
        
        return Response({'posts': UserAuthSerializer(instance).data})
            
    def post(self, request):
            if User.objects.filter(email=request.data.get('email')).exists():
                user = User.objects.get(email=request.data.get('email'))
                if user.username is None and user.password=='':
                    user.delete()
                else:
                    return Response({"error": "Пользователь уже зарегестрирован"})
            try:
                serializer = UserInvitationSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                user = User.objects.get(email=serializer.data.get('email'), token=serializer.data.get('token'))

                Role.objects.filter(user__id=user.id, role='initializer').delete()
                role_serializer = RoleSerializer(data = {'user': user.pk, 'role':'initializer'})
                role_serializer.is_valid(raise_exception=True)
                role_serializer.save()

                user_role = Role.objects.get(user__id=user.id, role='initializer')

                user.roles.add(user_role)
                user.email_user(
                    'Приглашение',
                    f'Ссылка на приглашение localhost:2222/api/v1/invite/{user.token}/',
                    from_email='settings.EMAIL_HOST_USER',
                    )
                
                return Response({"success": "Успешное приглашение пользователя"})
            except:
                return Response({"error": "Ошибка приглашения пользователя"})
    
    def put(self, request, *args, **kwargs):
        token = kwargs.get('token', None)
        if not token:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            instance = User.objects.get(token=token)
        except:
            return Response({'error': 'Object does not exist'})
        
        serializer = UserAuthSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'put': serializer.data})
                
