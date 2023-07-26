from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Idea
from .serializers import IdeaSerializer

class IdeasViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

# Create your views here.
