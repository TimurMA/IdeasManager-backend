from core.utils.read_request_file import read_request_file
from core.utils.extract_emails import extract_emails_from_content
from core.utils.send_message_async import EmailThread

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserAuthSerializer, RoleSerializer, UserInvitationSerializer
from .models import User, Role

from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.utils import timezone

from datetime import timedelta

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
                return Response({
                    "user": UserAuthSerializer(user).data,
                    'roles': [role.role for role in user.roles.all()]
                    })
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
            return Response({'error': 'Вы не приглашены'})
        print(instance.date_joined + timedelta(days=+3))
        print(timezone.now())
        if instance.date_joined + timedelta(days=+3) < timezone.now():
            instance.delete()
            return Response({'error': 'Срок приглашения истек'})

        return Response({'posts': UserAuthSerializer(instance).data})
            
    def post(self, request):
        if request.data.get('uploaded_file', ''):
            try:
                readed_file = read_request_file(request.data.get('uploaded_file', ''))
            except:
                return Response({
                    'error': 'Неверный формат фаила'
                })
            emails = extract_emails_from_content(readed_file)
        elif request.data.get('emails', ''):
            emails = request.data.get('emails')
        else:
            return Response({
                'error': 'Введите электронные адреса для отправки приглашений'
            })
        if not request.data.get('roles', ''):
            return Response({
                'error': 'добавьте роли'
            })
        else:
            roles = request.data.get('roles')
        

        try:
            for email in emails:
                if User.objects.filter(email=email).exists():
                    user = User.objects.get(email=email)
                    if user.username is None and user.password=='':
                        user.delete()
                    else:
                        continue
                
                serializer = UserInvitationSerializer(data={'email': email})
                serializer.is_valid(raise_exception=True)
                serializer.save()

                user = User.objects.get(email=serializer.data.get('email'), token=serializer.data.get('token'))


                for role in roles:
                    Role.objects.filter(user__id=user.id, role=role).delete()
                    role_serializer = RoleSerializer(data = {'user': user.pk, 'role':role})
                    role_serializer.is_valid(raise_exception=True)
                    role_serializer.save()

                    user_role = Role.objects.get(user__id=user.id, role=role)

                    user.roles.add(user_role)
                    
                EmailThread(
                    subject='Приглашение', 
                    message=f'Ссылка на приглашение localhost:2222/api/v1/invite/{user.token}/',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_user=user.email
                    ).start()
                
            return Response({"success": "Успешное приглашение пользователей"})
        except:
            return Response({"error": "Ошибка приглашения пользователей"})
    
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

        return Response({
                    "user": serializer.data,
                    'roles': [role.role for role in instance.roles.all()]
                    })
                
