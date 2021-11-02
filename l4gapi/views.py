# We import the views
from rest_framework import viewsets

# We import the created serializers
from .serializers import ServerSerializer
# We import the created models
from .models import Server


# We indicate what to serialise
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('server_id')
    serializer_class = ServerSerializer

