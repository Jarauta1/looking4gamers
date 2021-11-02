from django.db import models
from django.conf import settings
from django.utils import timezone

# Server table with fields id (primary key), server name, members and groups

class Server(models.Model):

    # Properties
    # Automatic ID, increases by one value with each new record
    server_id = models.BigAutoField(primary_key=True)
    server_name = models.CharField(max_length=50)
    members = models.JSONField(blank=True, default=dict)
    groups = models.JSONField(blank=True, default=dict)

    # Magic method
    def __str__(self):
        return self.server_name
