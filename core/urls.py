from django.contrib import admin
from django.urls import path, include

from apps.auth.views import LoginAPI, InvitationRegisterAPI
from apps.ideas_manager.views import IdeasViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'ideas_manager', IdeasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', LoginAPI.as_view()),
    path('api/v1/invite/<str:token>/', InvitationRegisterAPI.as_view()),
    path('api/v1/invite/', InvitationRegisterAPI.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/ideas_manager/get_user_ideas/<str:token>/', IdeasViewSet.as_view({'get': 'list'}))
]
