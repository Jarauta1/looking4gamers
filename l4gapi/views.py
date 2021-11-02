# We import the views
from rest_framework import viewsets

# We import the created serializers
from .serializers import ServerSerializer, GroupSerializer, UsersSerializer, ChannelSerializer, MessageSerializer
# We import the created models
from .models import Server, Group, Users, Channel, Message


# We indicate what to serialise
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('server_id')
    serializer_class = ServerSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('group_id')
    serializer_class = GroupSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('msg_id')
    serializer_class = MessageSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('channel_id')
    serializer_class = ChannelSerializer
