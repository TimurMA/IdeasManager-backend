from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Idea
from .serializers import IdeaSerializer

class IdeasViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def list(self, request, *args, **kwargs):
        if kwargs.get('token', ''):
            data = self.get_queryset().filter(initiator=kwargs.get('token', ''))
            serializer_data = self.get_serializer(data, many=True)
            return Response(serializer_data.data)

        return super(IdeasViewSet, self).list(request, *args, **kwargs)

# Create your views here.
