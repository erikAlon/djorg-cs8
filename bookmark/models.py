from django.db import models
from uuid import uuid4


class Bookmarks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    addresses = models.CharField(max_length=200)
