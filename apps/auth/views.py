from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSignupSerializer, UserLoginSerializer
from .models import User

class LoginAPI(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            if user.password == request.data['password']:
                return Response({
                    "user": UserLoginSerializer(user).data
                })
            else:
                return Response({
                    'error': 'Пароль неверен'
                })
        except:
            return Response({
                    'error': 'Пользователя не существует'
                })


class SignupAPI(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'new_user': serializer.data
        })



