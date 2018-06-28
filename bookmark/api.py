from rest_framework import serializers, viewsets
from .models import Bookmarks


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ('url', 'name', 'addresses')


class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmarks.objects.all()
