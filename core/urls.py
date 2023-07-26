from django.contrib import admin
from django.urls import path, include

from apps.auth.views import SignupAPI, LoginAPI
from apps.ideas_manager.views import IdeasViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'idea_manager', IdeasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', LoginAPI.as_view()),
    path('api/v1/signup/', SignupAPI.as_view()),
    path('api/v1/', include(router.urls))
]
