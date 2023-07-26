from django.contrib import admin
from django.urls import path
from apps.auth.views import RegisterAPI, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', LoginAPI.as_view()),
    path('api/v1/register/', RegisterAPI.as_view()),
]
