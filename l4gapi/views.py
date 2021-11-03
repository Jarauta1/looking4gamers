# We import the views and filter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

# We import the created serializers
from .serializers import ServerSerializer, GroupSerializer, UsersSerializer, ChannelSerializer, MessageSerializer
# We import the created models
from .models import Server, Group, Users, Channel, Message


# We add restrictions to the set of views so that unauthorised users do not have access
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to your Server!"}
    return JsonResponse(content)


# We indicate what to serialise
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('server_id')
    serializer_class = ServerSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('group_id')
    serializer_class = GroupSerializer

    # Filter to can search by group name
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['group_name']


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('msg_id')
    serializer_class = MessageSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('channel_id')
    serializer_class = ChannelSerializer

    # Filter to can search by topic channel
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['topic']
