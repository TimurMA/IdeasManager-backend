from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserAuthSerializer
from .models import User

class LoginAPI(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            if user.password == request.data['password']:
                return Response({
                    "user": UserAuthSerializer(user).data
                })
            else:
                return Response({
                    'error': 'Ошибка авторизации'
                })
        except:
            return Response({
                    'error': 'Ошибка авторизации'
                })


class SignupAPI(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'user': serializer.data
        })



