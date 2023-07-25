from django.contrib import admin
from django.urls import path, include
from apps.auth.views import SignupAPI, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', LoginAPI.as_view()),
    path('api/v1/signup/', SignupAPI.as_view()),
]
