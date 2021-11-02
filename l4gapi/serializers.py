# Serialise the data model

# Import serializers
from rest_framework import serializers

# We bring with us the data models defined in the MER
from .models import Server

# Create the serializers for the models
class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('server_id', 'server_name', 'members', 'groups')
