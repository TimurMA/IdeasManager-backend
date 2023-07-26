from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserAuthSerializer
from .models import User

from django.contrib.auth.hashers import check_password


class LoginAPI(APIView):
    def post(self, request):
        try:
            user = User.objects.get(
                username=request.data["username"], role=request.data["role"]
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


class RegisterAPI(APIView):
    def post(self, request):
        try:
            serializer = UserAuthSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()
            return Response({"success": "Успешное добавление пользователя"})

        except:
            return Response({"error": "Ошибка регистрации пользователя"})
